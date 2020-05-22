from django.shortcuts import render
from .models import projects
from .models import Myeducation

# Create your views here.

def index(request):

   


    proj=projects.objects.all()

    edu=Myeducation.objects.all()


    return render(request,'index.html',{'proj':proj,'edu':edu})