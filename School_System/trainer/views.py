from django.shortcuts import render
from .forms import TrainersForm
from django.shortcuts import render
from .models import Trainer


def register_student(request):
    if request.method == "POST":
        form =TrainersForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=TrainersForm()
    return render (request,"trainer.html",{"form":form})

def trainers_list(request):
    trainers=Trainer.objects.all()
    return render(request,"trainers_list.html",{"trainers":trainers})

