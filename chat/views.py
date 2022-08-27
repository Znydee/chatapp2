from django.shortcuts import render
from django.contrib.auth.models import User   
from django.http import HttpResponse, JsonResponse
from .models import Message
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.utils.timesince import timesince
# Create your views here.
@login_required
def home(request):
    people=User.objects.all()
    return render(request,"chat/index.html",{"people":people})
    
def get_message(request):
    username = request.GET["username"]
    ins = User.objects.get(username=username)
    messages = Message.objects.filter(sender=request.user, reciever = ins)|Message.objects.filter(reciever=request.user, sender = ins)
    messages = messages.order_by("timestamp")
    messages=list(messages.values())
    for item in messages:
        item["timestamp"] = timesince(item["timestamp"])
        if item["timestamp"] == "0\xa0minutes":
             item["timestamp"] = "now"
        else:
            item["timestamp"] = f"{item['timestamp']} ago"
        #print(item["timestamp"])
    #print(messages)
    return JsonResponse({"messages": messages})
    
def register(request):    
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form=UserRegisterForm()            
    return render(request,"chat/register.html", {"form":form})