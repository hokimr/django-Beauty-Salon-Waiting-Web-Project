from dataclasses import field
from django import forms
from .models import waiting
from django.forms import ModelForm

class WaitingForm(ModelForm):
    class Meta:
        model = waiting
        fields ="__all__"