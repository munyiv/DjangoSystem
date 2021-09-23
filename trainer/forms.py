from django import forms
from django.forms import fields
from django .db import models
from .models import Trainer

class TrainersForm(forms.ModelForm):
    class Meta:
        model=Trainer
        fields="__all__"