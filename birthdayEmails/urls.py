from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^signup',views.signup, name="signup"),
    url(r'^createUser/(?P<code>[a-zA-Z0-9_]+)/',views.createUser, name="createUser"),
    url(r'^newTokenNeeded',views.newTokenNeeded, name="newTokenNeeded"),
    url(r'^signIn',views.signIn, name="signIn"),
    url(r'^signOut',views.signOut, name="signOut"),
    url(r'^main',views.main, name="main"),
    url(r'^toggle_patient_(?P<patient_id>\d+)/$',views.toggle_patient, name="toggle_patient"),
    url(r'^saveEmail',views.saveEmail, name="saveEmail"),
]