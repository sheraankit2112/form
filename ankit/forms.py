from django import forms
from django.contrib.auth.models import User


def email_validator(value):
    if User.objects.filter(email=value).exists():
        raise forms.ValidationError("Email already registered")

class detailform(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField(validators=[email_validator])

