from django.shortcuts import redirect, render
from .forms import CalenderForm
from django.shortcuts import render
from .models import Calender
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import datetime
from .utils import Calendar
from datetime import date



def register_calender(request):
    if request.method == "POST":
        form =CalenderForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=CalenderForm()
    return render (request,"calendar.html",
    {"form":form})

def calendar_list(request):
    calendar=Calender.objects.all()
    return render(request,"calendar_list.html",{"calendar":calendar})

class CalendarView(generic.ListView):
    model = Calender
    template_name = 'calendar_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, w/hich returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def calender_profile(request,id):
    calender=Calender.objects.get(id=id)
    return render(request,"calender_profile.html",{"calender":calender})

def edit_calender(request,id):
    calender=Calender.objects.get(id=id)
    if request.method == "POST":
        form=CalenderForm(request.POST, instance=calender)
        if form.is_valid():
            form.save()
        return redirect("trainer_profile",id=calender.id)
    else:
        form=CalenderForm(instance=calender)
        return render(request,"edit_calender.html",{"form":form})








