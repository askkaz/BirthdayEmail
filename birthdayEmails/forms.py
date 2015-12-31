from django import forms

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



#     <form action="{% url 'birthdayEmails:saveEmail' %}">
#     {% csrf_token %}
#     <div class="form-group">
#       <label for="patientName" class="form-label">Patient</label>
#       <input type="text" class="form-control" id="patientName" placeholder="Select one from the list..." disabled>
#     </div>
#     <div class="form-group">
#       <label for="emailSubject" class="form-label">Subject</label>
#       <input type="text" class="form-control" id="emailSubject" required>
#     </div>
#     <div class="form-group">
#       <label for="emailBody" class="form-label">Body</label>
#       <textarea class="form-control" id="emailBody" rows="3" required></textarea>
#     </div>
#     <input class="btn" type="submit" value="Add Email to Pending Queue">
# </form>