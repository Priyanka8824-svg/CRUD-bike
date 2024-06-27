from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import BikeForm
from .models import Bike
from django.contrib.auth.decorators import login_required

# Create your views here
def hview(request):
    return render(request,"app1/home.html",{})

@login_required(login_url="/a2/lv/")
def bview(request):
    form = BikeForm()
    if request.method == "POST":
        form = BikeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/bike_form.html",{"form":form})

@login_required(login_url="/a2/lv")
def sview(request):
    bi = Bike.objects.all()
    print(bi)
    return render(request,"app1/show.html",{"obj":bi})

def updateview(request,pk):
    obj = Bike.objects.get(series=pk)
    form = BikeForm(instance=obj)
    if request.method == "POST":
        form = BikeForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/bike_form.html",{"form":form})

def deleteview(request,x):

## Directly delete record ##
    # obj=Bike.objects.get(name=x)
    # obj.delete()
    # return redirect("/a1/sv/")

##confirm page##
    obj = Bike.objects.get(series=x)
    if request.method == "POST":
        obj.delete()
        return redirect("/a1/sv/")
    return render(request,"app1/success.html",{"obj":obj})
