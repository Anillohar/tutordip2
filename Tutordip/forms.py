from django.contrib.auth.forms import UserCreationForm
from django import  forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    number = forms.CharField(max_length=12)
    email=forms.EmailField(max_length=254, help_text='Required. Inform a valid email address')
    username = forms.CharField(max_length=254)
    password1=forms.CharField(max_length=257)
    password2 = forms.CharField(max_length=257)
    student = forms.BooleanField()
    class Meta:
        model= User
        fields = ('email', 'number', 'username', 'password1', 'password2','student')
    # def clean_username(self):
    #     data=self.cleaned_data['username'].lower()
    #     r=User.objects.filter(username=data)
    #     if r.count():
    #         raise ValidationError('User already exists')
    #     return  data
    #
    #
    # def clean_email(self):
    #     data=self.cleaned_data['email']
    #     e=User.objects.filter(email=data)
    #     if e.count():
    #         raise ValidationError('email already exists')
    #     return data
    #
    # def clean_password2(self):
    #     pass1=self.cleaned_data['password1']
    #     pass2=self.cleaned_data['password2']
    #     if pass1 and pass2 and pass1!=pass2:
    #         raise ValidationError('password do not match')
    #     return pass2