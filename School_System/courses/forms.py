from django import forms
from django.forms import fields
from django.db.models.base import Model
from .models import Courses

class CoursesForm(forms.ModelForm):
    class Meta:
        model=Courses
        fields="__all__"