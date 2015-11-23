from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .common.drchronoUtils import *
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import TempUser, DrchronoUser, User

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
    return render(request, 'birthdayEmails/main.html', {'patient_list': patient_details})

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


