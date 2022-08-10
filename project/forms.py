from django import forms
from django.contrib.auth.models import User
from . import models


class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','password']

class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['name','author','isbn','publisher']        