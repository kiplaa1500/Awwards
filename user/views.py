from django.shortcuts import render,redirect,get_object_or_404
import datetime as dt
from .models import *

# Create your views here.

def home(request):
    date = dt.date.today()
    projects = Projects.objects.all()
    return render(request, 'index.html', {"date": date,"projects":projects})

# View funtion to return project by id
def get_project_by_id(request, id):

    try:
        project = Projects.objects.get(pk = id)
        
    except ObjectDoesNotExist:
        raise Http404()    
    
    return render(request, "project.html", {"project":project})
