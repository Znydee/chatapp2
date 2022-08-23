from django.shortcuts import render
from django.contrib.auth.models import User   
# Create your views here.
def home(request):
    people=User.objects.all()
    return render(request,"chat/index.html",{"people":people})