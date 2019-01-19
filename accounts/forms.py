from django import forms
from django.db import models
from accounts.models import UserProfile
from accounts.models import Transactions
import datetime
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
# from django.forms.extras.widgets import SelectDateWidget

class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"




from .models import User


class UserRegistrationForm(UserCreationForm):
    birth_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        model = UserProfile
        fields = [
                  "full_name",
                  "birth_date",
                  "email",
                  "contact_no",
                  "Address",
                  "city",
                  "country",
                  "nationality",
                  "occupation",
                  "password1",
                  "password2"
                  ]

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['full_name']
        user.birth_date = self.cleaned_data['birth_date']
        if commit:
            user.save()
        return user


class Deposit_form(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = [
            'amount'
        ]

class Withdrawl_form(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = [
            'amount'
        ]