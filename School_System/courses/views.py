from django.shortcuts import render
from .forms import CoursesForm
from django.shortcuts import render
from .models import Courses

def register_student(request):
    if request.method == "POST":
        form =CoursesForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=CoursesForm()
    return render (request,"courses.html",{"form":form})

def courses_list(request):
    courses=Courses.objects.all()
    return render(request,"courses_list.html",{"courses":courses})
