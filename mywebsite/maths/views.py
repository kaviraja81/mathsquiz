from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .forms import AdditionForm,RegisterForm
from .validate import calcscore,validate

# Create your views here.


def index(request):
    return HttpResponse("This is the addition view")



# val=[response.POST.get('inputans{}'.format(i)) for i in range(1,11)]
 


def add(response):
    global result
    global num1, num2

    if response.method == "POST":
        output = response.POST.getlist('inputans')
        print(num1, num2)
        validoutput, IsValid = validate(output)
        print(validoutput, output, IsValid)
        if not IsValid:
            zippedlist = zip(num1, num2, validoutput, output)
            return render(response, "maths/addition.html", {"zippedlist": zippedlist})
        else:
            output = [int(i) for i in output]
            score = calcscore(output, result)

            return HttpResponse(f'Good Job! Your Score is {score} /10')
    else:
        form1 = AdditionForm()
        num1 = form1.randnum()
        num2 = form1.randnum()
        output = [0 for i in range(10)]
        validval = [True for i in range(10)]
        zippedlist = zip(num1, num2, validval, output)
        result = num1+num2
        validval = [True for i in range(10)]
        return render(response, "maths/addition.html", {"zippedlist": zippedlist})

def register(request):

    form=RegisterForm()

    return render(request,"maths/register.html",{"form":form})
