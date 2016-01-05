from django import forms
from django.forms.extras.widgets import SelectDateWidget
from datetime import date

class EmailForm(forms.Form):
    patientId = forms.CharField(
        label='Patient Id', 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly',
            'id': 'patientId',
            'type': 'hidden'}))
    patientBirthday = forms.CharField(
        label='Patient Birthday', 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly',
            'id': 'patientBirthday',
            'type': 'hidden'}))
    patientEmailAddress = forms.CharField(
        label='Patient Email', 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly',
            'id': 'patientEmailAddress',
            'type': 'hidden'}))
    patientName = forms.CharField(
        label='Patient', 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'required': 'true',
            'class': 'form-control',
            'readonly': 'readonly',
            'placeholder': 'Select one from the list...',
            'id': 'patientName'}))
    emailSubject = forms.CharField(
        label='Subject',
        max_length=100,
        widget=forms.TextInput(attrs={
            'required': 'true',
            'class': 'form-control',
            'id': 'emailSubject'}))
    emailBody = forms.CharField(
        label='Body',
        widget=forms.Textarea(attrs={
            'required': 'true',
            'class': 'form-control',
            'id': 'emailBody',
            'rows': '3'
            }))

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'required': 'true',
            'name': 'username',
            'placeholder': 'username',
            'class': 'form-control',
        }))
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={
            'required': 'true',
            'name': 'password',
            'placeholder': 'password',
            'class': 'form-control',
        }))

class CreateAccountForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'required': 'true',
            'name': 'username',
            'placeholder': 'username',
            'class': 'form-control',
        }))
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={
            'required': 'true',
            'name': 'password',
            'placeholder': 'password',
            'class': 'form-control',
            'pattern': '.{5,}',
            'required title': '5 characters minimum',
        }))