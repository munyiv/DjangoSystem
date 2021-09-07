from django.shortcuts import redirect, render
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

def trainer_profile(request,id):
    trainer=Trainer.objects.get(id=id)
    return render(request,"trainer_profile.html",{"trainer":trainer})

def edit_trainer(request,id):
    trainer=Trainer.objects.get(id=id)
    if request.method == "POST":
        form=TrainersForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
        return redirect("trainer_profile",id=trainer.id)
    else:
        form=TrainersForm(instance=trainer)
        return render(request,"edit_trainer.html",{"form":form})


