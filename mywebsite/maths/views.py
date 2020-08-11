from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .forms import AdditionForm


def validate(output):
    valid=[]

    IsValid=True
    for i in range(10):
            
          if output[i] == '' or  (not output[i].isnumeric()) : 
            valid.insert(i,False)
            IsValid = False
          else: 
            valid.insert(i,True)
    return valid,IsValid

# Create your views here.
def index(request):
    return   HttpResponse("This is the addition view")


def calcscore(output,correctresult):
    score=0
    for i in range(10):
        if correctresult[i] == output[i]: 
            score +=1
            print ("All right f{i}") 
        else : 
            print("Some Wrong") 
# val=[response.POST.get('inputans{}'.format(i)) for i in range(1,11)] 
    return score

def add(response):
    global result
    global num1,num2
    # result=[]
    # form2=AdditionForm() 
    # print(result)
    if response.method =="POST":
        output=response.POST.getlist('inputans')   
        print(num1,num2)
        validoutput,IsValid=validate(output)
        print (validoutput,output,IsValid)
        if not IsValid : 
            zippedlist=zip(num1,num2,validoutput,output)
            return render(response,"maths/addition.html",{"zippedlist":zippedlist})
        else :
            output=[int(i) for i in output ]
            score=calcscore(output,result)
            
            return HttpResponse(f'Good Job! Your Score is {score} /10')
    else:
        form1=AdditionForm()             
        num1=form1.randnum()
        num2=form1.randnum()
        output=[0 for i in range(10)]
        validval=[True for i in range(10)]
        zippedlist=zip(num1,num2,validval,output)
        result=num1+num2
        validval=[True for i in range(10)]
        return render(response,"maths/addition.html",{"zippedlist":zippedlist})
    
  