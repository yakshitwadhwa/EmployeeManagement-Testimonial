from django.http  import HttpResponse
import datetime
from django.shortcuts import render

def test(request):
    if request.method=='POST':
        check = request.POST.get('ab')
        print(check)
        if check is None:isActive=False
        else:isActive=True
        print(isActive)


    
    date = datetime.datetime.now()
    isActive = True
    name ="Learnwith me "
    list_of_program=[
        'WAP to check evem or odd',
        'WAP to check prime or odd',
        'WAP to print n 1 to 100'
    ]
    student ={
        "studentname" :"rahul",
        "studentcollege":"XYZ",
        "studentcity":"Rohtak"
    }
    data={
        "isActive":isActive,
        "name":name,
        "list_of_program":list_of_program,
        "Student_data":student

    }

    
    # print("Hello")  # ✅ Properly aligned
    # return HttpResponse("<h1>hello this is index page</h1>"+str(date))
    return render(request,"test.html",data)

def about(request):
    # return HttpResponse("This is about page")
    return render(request,"about.html",{})
def services(request):
    # return HttpResponse("This is services page")
    return render(request,"services.html",{})