# your_app/forms.py
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)





class CustomerVerificationForm:
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    address = forms.CharField(max_length=255)
    id_type = forms.ChoiceField(
        choices=[('passport', 'Passport'), ('driver_license', "Driver's License"), ('national_id', 'National ID')])
    id_number = forms.CharField(max_length=20)

    from django import forms

class FeedbackForm(forms.Form):
        name = forms.CharField(max_length=100)
        email = forms.EmailField()
        feedback = forms.CharField(widget=forms.Textarea)
