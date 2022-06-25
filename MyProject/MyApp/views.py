from django.shortcuts import render,redirect
from django.http import HttpResponse
from MyApp.models import Student

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

def boot(request):
	return render(request,'MyApp/boot.html')

def offline(request):
	return render(request,'MyApp/offline.html')

def get(request):
	if request.method=="POST":
		na=request.POST['uname']
		mb=request.POST['mbl']
		em=request.POST['email']
		ps=request.POST['psw']
		cps=request.POST['cpsw']
		do=request.POST['dob']

		return render(request,'MyApp/details.html',{'us':na,'m':mb,'e':em,'p':ps,'cp':cps,'d':do})

	return render(request,'MyApp/get.html')

def insert(request):
	if request.method=="POST":
		na=request.POST['name']
		roll=request.POST['rollnum']
		age=request.POST['age']
		mbl=request.POST['mbl']
		em=request.POST['email']
		add=request.POST['addr']

		Student.objects.create(name=na,rollnum=roll,age=age,mobile=mbl,
			email=em,address=add)
		return redirect('/read')
	return render(request,'MyApp/insert.html')


def read(request):
	data=Student.objects.all()
	return render(request,'MyApp/read.html',{'data':data})

def update(request,id):
	data=Student.objects.get(id=id)
	if request.method=="POST":
		data.name=request.POST['name']
		data.rollnum=request.POST['rollnum']
		data.age=request.POST['age']
		data.mobile=request.POST['mbl']
		data.email=request.POST['email']
		data.address=request.POST['addr']
		data.save()
		return redirect('/read')
	return render(request,'MyApp/update.html',{'data':data})

def delete(request,id):
	ob=Student.objects.get(id=id)
	if request.method=="POST":
		ob.delete()
		return redirect('/read')
	return render(request,'MyApp/delete.html',{'info':ob})