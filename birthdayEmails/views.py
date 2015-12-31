from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .common.drchronoUtils import *
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import EmailForm
import pytz

from .models import TempUser, DrchronoUser, User, DrchronoEmail

def index(request):
    return render(request, 'birthdayEmails/login.html', {'link_url': getDrchronoLinkURL()})

def signup(request):
    code = request.GET.get('code')
    if not code:
        return HttpResponseRedirect(reverse('birthdayEmails:index'))
    else:
        auth_data = getDrchronoAuth(code)
        #TODO - add check for no data back (bad code)
        auth_data['code'] = code
        TempUser.objects.create(**auth_data)
        return render(request, 'birthdayEmails/signup.html', {
            'code': code
        })

def success(request, code):
    return HttpResponse('THANKS')

def newTokenNeeded(request):
    return render(request, 'birthdayEmails/newtoken.html')

def invalidSignUpCredentials(request, code):
    return render(request, 'birthdayEmails/signup.html', {
        'code': code
    })

def createUser(request, code):
    if request.method == "POST":
        #ensure the code was a recent token (5 minutes seems reasonable)
        temp_user_data = TempUser.objects.filter(code=code, created__gte=timezone.now()-datetime.timedelta(minutes=5)).first()
        if temp_user_data:
            password = request.POST['password']
            username = request.POST['username']
            if len(password) < 5 or User.objects.filter(username=username):
                return render(request, 'birthdayEmails/invalidsignupcredentials.html', {'code':code})
            drchrono_user = User.objects.create_user(username, None, password)
            birthday_user = DrchronoUser(user=drchrono_user, access_token=temp_user_data.access_token, 
                refresh_token=temp_user_data.refresh_token, expires_timestamp=temp_user_data.expires_timestamp)
            birthday_user.save()
            return HttpResponseRedirect(reverse('birthdayEmails:success', args=(code,)))
        else:
            return HttpResponseRedirect(reverse('birthdayEmails:newTokenNeeded'))

@login_required
def main(request):
    logged_in_user = DrchronoUser.objects.filter(user = request.user)[0]
    logged_in_user.check_access_token()
    access_token = logged_in_user.access_token
    patient_details = getDrchronoPatientDetails(access_token)
    form = EmailForm()
    #attach patient details to each of the two records and remove from patient details array
    for i in range(len(patient_details)):
        emails = DrchronoEmail.objects.filter(
            patient_id=patient_details[i]['id']
        ).filter(
            user=request.user.id
        ).filter(
            Q(sent_date__isnull=True) | Q(sent_date__gt=timezone.now()-datetime.timedelta(weeks=4))
        ).order_by(
            '-send_date'
        )
        if len(emails) > 0:
            patient_details[i]['birthdayEmail'] = emails[0]
        else:
            patient_details[i]['birthdayEmail'] = ""
    return render(request, 'birthdayEmails/main.html', {'patient_list': patient_details, 'form': form})

def signIn(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('birthdayEmails:main'))
        else:
            # Return a 'disabled account' error message
            return HttpResponse('INACTIVE')
    else:
        # Return an 'invalid login' error message.
        return HttpResponse('BAD')

@login_required
def signOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('birthdayEmails:index'))

@login_required
def toggle_patient(request, patient_id):
    return render_to_response({"test":"test"})

@login_required
def saveEmail(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form_data = form.cleaned_data
            action = request.POST['button']
            birthday = pytz.utc.localize(datetime.datetime.strptime(form_data['patientBirthday'], "%Y-%m-%d"))
            now = timezone.now()
            this_year = now.year
            send_date = birthday.replace(year=this_year,hour=0, minute=1)
            if send_date < now:
                send_date = send_date.replace(year=this_year+1)
            this_user = DrchronoUser.objects.filter(user=request.user.id)[0]
            this_patient = form_data['patientId']
            existing_email = DrchronoEmail.objects.filter(user = this_user).filter(patient_id = this_patient).order_by('-send_date').first()
            if action == 'Save':
                if existing_email:
                    existing_email.body = form_data['emailBody']
                    existing_email.subject = form_data['emailSubject']
                    existing_email.save()
                else:
                    email = DrchronoEmail.objects.create(
                        send_date = send_date,
                        subject = form_data['emailSubject'],
                        body = form_data['emailBody'],
                        patient_id = this_patient,
                        user = this_user)
            elif action == 'Delete':
                existing_email.delete()

            return HttpResponseRedirect(reverse('birthdayEmails:main'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmailForm()

    return HttpResponseRedirect(reverse('birthdayEmails:main'))


