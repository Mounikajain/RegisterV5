from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import ShowModel
from django.contrib import messages

# Create your views here.
def showindex(request):
    qs = ShowModel.objects.all()
    return render(request, "index.html", {"data": qs})


def reg_save(request):
    fname = request.POST.get("first_name")
    lname = request.POST.get("last_name")
    mail = request.POST.get("email")
    cname = request.POST.get("college_name")
    gen = request.POST.get("gender")
    Pno = request.POST.get("phone_no")
    sta = request.POST.get("state")
    cit = request.POST.get("city")
    idea = request.POST.get("idea")
    problem = request.POST.get("problem")
    academic = request.POST.get("academic")
    link = request.POST.get("link")
    team = request.POST.get("team")
    hack_b = request.POST.get("hack_b")
    hear = request.POST.get("hear")
    sm=ShowModel(First_name=fname,Last_name=lname,Email=mail,college_Name=cname,gender=gen,phone_No=Pno,state=sta,city=cit,idea=idea,problem=problem,academic=academic,link=link,team=team,hack_befor=hack_b,hack_heard=hear)
    sm.save()
    messages.success(request,"Registered Successfully")
    return HttpResponse("<html><body><center><h1>Registered Successfully</h1></center></body></html>")


