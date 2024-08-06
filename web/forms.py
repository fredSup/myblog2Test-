from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.db.models.base import Model
from django.forms import fields
from django.contrib.auth.models import User
import re




class UserForm(forms.Form):
    class Meta:
        model = User
        fields = ('last_name', 'first_name') 



class LoginForm(forms.Form):
    username = forms.EmailField(label="Email")
    password = forms.CharField(label="Mot de passe")