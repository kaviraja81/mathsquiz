from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from django.contrib import messages


from django.contrib.auth.forms import UserCreationForm
from .forms import AdditionForm,RegisterForm
from .validate import calcscore,validate
from django.contrib.auth  import login,logout,authenticate 
from .models import User
from maths.models import Score 
# Create your views here.


def index(request):
  #  return HttpResponse("This is the addition view")
    return render(request, "maths/homepage.html", {})



# val=[response.POST.get('inputans{}'.format(i)) for i in range(1,11)]

def grade(response):
    return render(response,"maths/grade.html",{})


def add(response,category):
    global result
    global num1, num2
    operator = '+'
    print(response.get_full_path())
    # print(response.path)
    # print(response.build_absolute_uri())
    valsplit=response.path.split('/')
    if valsplit[2] == 'add' :
       operator = '+'
    elif valsplit[2] == 'sub':
        operator = '-'
    

    print (operator)
    if response.method == "POST":
        output = response.POST.getlist('inputans')
        print(num1, num2)
        print(output)
        validoutput, IsValid = validate(output)
        print(validoutput, output, IsValid)
        
        if not IsValid:
            print("not valid")
            zippedlist = zip(num1, num2, validoutput, output)
            return render(response, "maths/addition.html", {"zippedlist": zippedlist,"operator": operator})
            
        else:
            output = [int(i) for i in output]
            score = calcscore(output, result)
            username = User.objects.get(username=response.user.username)

         #   username=response.user.username
            t=Score(score=score,grade=valsplit[1][5],category=valsplit[3],username=username)
            t.save()
            
            return HttpResponse(f'Good Job! Your Score is {score} /10')
    else:
        ##  Category 1 is Single Digit Addition, 
        ##  Category 2 is Double Digit Addition
        #3  Category 3 is Additions with Tens
        ##  Category 4 is Single Digit Subtraction 
        ##  Category 5 is Double Digit Subtraction
        ##  Category 6 is Subtraction wtih tens
        form1 = AdditionForm()
        if category == 1 or category == 4 :
            num1 = form1.randnumsingledigit()
            num2 = form1.randnumsingledigit()
        elif category == 2 or category == 4: 
            num1 = form1.randnumdoubledigit()
            num2 = form1.randnumdoubledigit()
        elif category == 3 or category == 6 :
            num1 = form1.randnumsingledigit()
            num2 = form1.randnumsingledigit()*10 
            
        # if operator == '-' :
        #     [x for x,y in num1 if num1 > num2 else: y  ]
        #    if num1 > num2 : 
        #       print (num1 > num2) 

        output = ['' for i in range(10)]
        validval = [True for i in range(10)]
        zippedlist = zip(num1, num2, validval, output)
        if operator == '+' :  result = num1+num2 
        else : result = num1-num2
        validval = [True for i in range(10)]
        context={}
        return render(response, "maths/addition.html", {"zippedlist": zippedlist,"operator": operator})

def register(request):
    
    if request.method=="POST" :
        form=RegisterForm(request.POST)
        if form.is_valid():
           form.save()
           username=form.cleaned_data.get("username")
           messages.success(request,f'New User {username} created successfully . Welcome {username}')
           print(username)
       #    login(request, username)
#           return redirect("/")
        else:
            for msg in form.error_messages:
                messages.error(request,f' {msg}: {form.error_messages[msg]}')
            return render(request,"maths/register.html",{"form":form})
    form=RegisterForm()
   
    return render(request,"maths/register.html",{"form":form})
