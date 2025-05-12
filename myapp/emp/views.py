from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp,Testimonial
# Create your views here.
def emp_home(request):
    emps=Emp.objects.all()
    return render(request,"emp/home.html",{'emps':emps})


def add_emp(request):
    if request.method=="POST":
        # data fetch 
        name=request.POST.get("empname")
        empid=request.POST.get("empid")
        phone=request.POST.get("empphone")
        address=request.POST.get("empaddress")
        empworking=request.POST.get("empworking")
        empdepartment=request.POST.get("empdepartment")
        # create model object and set the data
        e=Emp()
        e.name=name
        e.emp_id=empid
        e.phone=phone
        e.address=address
        e.department=empdepartment
        if empworking is None:
            e.working=False
        else:
            e.working=True
        # save the object 
        e.save()          
        # prepare msg
        print("data is coming")
        return redirect("/emp/")
    return render(request,"emp/add.html",{})

def delete(request,emp_id):
    print(emp_id)
    emp =Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/")

def update(request,emp_id):
    emp = Emp.objects.get(pk=emp_id)
    return render(request,"emp/update.html",{'emp':emp})

def doupdate(request,emp_id):
    if request.method=='POST':
        name=request.POST.get("empname")
        empidtemp=request.POST.get("empid")
        phone=request.POST.get("empphone")
        address=request.POST.get("empaddress")
        empworking=request.POST.get("empworking")
        empdepartment=request.POST.get("empdepartment")
        e=Emp.objects.get(pk=emp_id)
        e.name=name
        e.emp_id=empidtemp
        e.phone=phone
        e.address=address
        e.department=empdepartment
        if empworking is None:
            e.working=False
        else:
            e.working=True
        e.save()   
    return redirect("/emp/")


def testimonials(request):
    test=Testimonial.objects.all()
    return render(request,"emp/testimonial.html",{'test':test})
