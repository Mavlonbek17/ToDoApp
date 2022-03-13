from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms



class NewTaskForm(forms.Form):
    task = forms.CharField(label="New task")

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request,"tasks/index.html",{
        "tasks":request.session["tasks"]
    })

def add(request):
    if request.method =="POST":
        userform = NewTaskForm(request.POST)
        if userform.is_valid():
            usertasks = userform.cleaned_data["task"]
            request.session["tasks"] += [usertasks]
            return HttpResponseRedirect(reverse("tasks:add"))
        else:
            return render(request,"tasks/add.html",{
                "form":userform
            })
    return render(request,"tasks/add.html",{
        "form":NewTaskForm()
    })