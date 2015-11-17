from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .common.drchronoUtils import *

def index(request):
    return HttpResponse('<a href="https://drchrono.com/o/authorize/?redirect_uri=http%3A//testingbirthdayapp.com%3A8000/birthdayEmails/signup&response_type=code&client_id=zWgcsmzbQdkPZOf1YJBP63Ou0Ln0V7AqAF8kHWTq">Create Birthday Email Account through drchrono</a>')

def signup(request):
    code = request.GET.get('code')
    if not code:
        return HttpResponseRedirect(reverse('birthdayEmails:index'))
    else:
        auth_data = getDrchronoAuth(code)
        return HttpResponse("Your link code is %s. Your access_token is %s." % (code, auth_data['access_token']))