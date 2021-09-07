from django.shortcuts import redirect, render
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

def courses_profile(request,id):
    courses=Courses.objects.get(id=id)
    return render(request,"courses_profile.html",{"courses":courses})

def edit_courses(request,id):
    courses=Courses.objects.get(id=id)
    if request.method == "POST":
        form=CoursesForm(request.POST, instance=courses)
        if form.is_valid():
            form.save()
        return redirect("courses_profile",id=courses.id)
    else:
        form=CoursesForm(instance=courses)
        return render(request,"edit_courses.html",{"form":form})




