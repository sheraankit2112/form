from django.shortcuts import redirect,render

from django.contrib.auth.models import User
from ankit.forms import detailform


def index(request):
    fm=detailform()
    if request.method=="POST":
        fm=detailform(request.POST)

        if fm.is_valid():
            name=fm.cleaned_data["name"]
            age=fm.cleaned_data["age"]
            email=fm.cleaned_data["email"]

            new=User.objects.create_user(username=name,email=email,password="ankit").save()
            return redirect("/welcome")

    return render(request,"index.html",{"form":fm})

def welcome(request):
    return render(request,"welcome.html")