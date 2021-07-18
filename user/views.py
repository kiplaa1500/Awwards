from django.shortcuts import render,redirect,get_object_or_404
import datetime as dt
# Create your views here.

def home(request):
    date = dt.date.today()
    projects = Projects.objects.all()
    return render(request, 'index.html', {"date": date,"projects":projects})
