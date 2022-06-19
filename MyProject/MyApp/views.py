from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sam(request):
	return HttpResponse("Hai guys welcome to django online session")

def hello(request):
	return HttpResponse("<h2>Hello world!</h2>")

def style(request):
	return HttpResponse("<h3 style=color:blue;background-color:green;font-style:italic;font-size:30px>Django workshop</h3>")

def dyn(request,id):
	return HttpResponse("<h3 style= background-color:red>My roll number is {}</h3>".format(id))

def home(request,name):
	return HttpResponse("<h2 style=background-color:green>My name is:{}</h2>".format(name))

def task(request,name,id):
	return HttpResponse("My name is: {} and My rollnumber is:{}".format(name,id))

def temp(request):
	return render(request,'MyApp/task.html',{})

def table(request):
	return render(request,'MyApp/table.html')

def register(request):
	return render(request,'MyApp/register.html')

def data(request,name,id):
	return render(request,'MyApp/data.html',{'n':name,'i':id})

def inline(request):
	return render(request,'MyApp/inline.html')

def internal(request):
	return render(request,'MyApp/internal.html')

def external(request):
	return render(request,'MyApp/external.html')