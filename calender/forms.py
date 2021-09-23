from django import forms
from django.forms import fields
from django.db.models.base import Model
from .models import Calender

class CalenderForm(forms.ModelForm):
    class Meta:
        model=Calender
        fields="__all__"

        
        widgets={
                    "event_name":forms.TextInput( attrs={'class': 'form-control','style':'width:99%','placeholder':'Event Name','id':'forminput'}),
                    "venue":forms.TextInput( attrs={'class': 'form-control','style':'width:99%','placeholder':'Venue','id':'forminput'}),
                    "start_time":forms.DateTimeInput(attrs={'class': 'form-control','placeholder':'Start Time','id':'forminput','type': 'datetime-local'}),
                    "end_time":forms.DateTimeInput(attrs={'class': 'form-control','placeholder':'End Time','id':'forminput','type': 'datetime-local'}),
                    # "description":forms.Textarea( attrs={'class': 'form-control','style':'width:99%','placeholder':'Description','id':'forminput'}),
                }