from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomerUser


class CustomerUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='이메일')

    class Meta:
        model = CustomerUser
        fields = UserCreationForm.Meta.fields + ('email', 'nickname')
