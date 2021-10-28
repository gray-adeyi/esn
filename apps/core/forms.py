from django import forms
from django.forms import fields
from . import models

class PassportForm(forms.ModelForm):
    class Meta:
        model = models.Member
        fields = '__all__'