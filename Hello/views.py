from django.shortcuts import render
from django.http import HttpResponse   # 2.after installing app in settings ,this views import httpresponse
from django import forms       # 9.3
from . forms import studentform                   # 9.4
from . models import students         # 10.3

# Create your views here.
form = studentform()                               # 9.5
my_dict={"insert_me":"its lowest..........","sr":"star dust","n":300, 'form':form} # 9.6  # 5.4 we can use any variable within the flower brackets ({{n}} to assign the text and variable-->

def index(request):                             # 2.1 creating simple function index and request(default) is defaultresponse
    return HttpResponse("<h1> I started learning django and its fun </h1>")              # 2.2 we will get http response

def Hello(request):
    # return HttpResponse("<h2> I am coming from the application urls.py file </h2>")            #4.2
     if request.method == "POST":                          # 10.4
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
     else:
        form = studentform()

     return render(request,'Hello/Home.html',context=my_dict) # (5.5 (context=my_dict) this is the variable mentioned in 5.4)), # [(5.1 template(folder), Hello(template_folder), Home(hello file))path]
      # writing the my_dict variable in context w2hrn hy

def list_view(request):                   # 10.5    to read the data present n the table students
    # dictionary for intial data with
    # field name as keys
    context = {}    #  empty dictionary

    # add the dictionary during intialization
    context["dataset"] = students.objects.all()      # dataset(key)  reads the all objects present in the class students in models and gives array as an output
    return render(request, "Hello/list_view.html", context)









