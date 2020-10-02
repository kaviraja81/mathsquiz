from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from django.contrib import messages

import plotly.express as px
from django.contrib.auth.forms import UserCreationForm
from .forms import AdditionForm,RegisterForm
from .validate import calcscore,validate
from django.contrib.auth  import login,logout,authenticate 

from .models import User
from maths.models import Score 
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

from io import StringIO

# Create your views here.


def index(request):
  #  return HttpResponse("This is the addition view")
    return render(request, "maths/homepage.html", {})

# val=[response.POST.get('inputans{}'.format(i)) for i in range(1,11)]

def grade(request):
    return render(request,"maths/grade.html",{})

def report(request):
    if not request.user.is_authenticated:
        return HttpResponse("<h2>Please login to see the report </h2> <a class='button' href='/login'>Login</a>" )
    username = User.objects.get(username=request.user.username)
    scrobject=Score.objects.filter(username=username)
    fig,ax = plt.subplots()
   
    avgscr=[]
    ctgry=[]
    for i in scrobject.all():
        avgscr.append(i.averagescore)
            
        if i.category == '1' :
            ctgry.append('Single Digit Addition')
        elif i.category== '2':
            ctgry.append('Double Digit Addition') 
        elif i.category == '3' :
            ctgry.append('Addition with Tens')
        elif i.category == '4' :
            ctgry.append('Single Digit Subtraction')
        elif i.category == '5' :
            ctgry.append('Double Digit Subtraction')
        elif i.category == '6': 
            ctgry.append('Subtraction with Tens')
        
    
    ax.set_title("Average Score for each category",color="darkblue")
    ax.set_xlabel("Category")
    ax.set_ylabel("Average Score")
    ax.bar(ctgry,avgscr)
    imgdata=StringIO()
    fig.savefig(imgdata,format='svg')
    imgdata.seek(0)
    plot_data=imgdata.getvalue()
  
    return render(request,"maths/report.html",{"score":Score.objects.filter(username=username),"plot":plot_data},)

def mathematics(request,category):
    global result
    global num1, num2
    operator = '+'
   # print(request.get_full_path())
    
    valsplit=request.path.split('/')
    if valsplit[2] == 'add' :
       operator = '+'
    elif valsplit[2] == 'sub':
        operator = '-'
    
    if request.method == "POST":
        output = request.POST.getlist('inputans')
        validoutput, IsValid = validate(output)
        
        if not IsValid:
            zippedlist = zip(num1, num2, validoutput, output)
            return render(request, "maths/addition.html", {"zippedlist": zippedlist,"operator": operator})
            
        else:
            
            output = [int(i) for i in output]
            score = calcscore(output, result)
            username = User.objects.get(username=request.user.username)
            try :
                t=Score.objects.get(username=username,category=valsplit[3],grade=valsplit[1][5])
                t.score=score
                t.totalattempts+=1
                t.averagescore=int((t.averagescore+score)/(t.totalattempts)) 
                t.save(update_fields=['totalattempts','averagescore','score'])
            except Score.DoesNotExist : 
               
                totalattempts = 1
                average=score/totalattempts
                t=Score(username=username,category=valsplit[3],grade=valsplit[1][5],score=score,
                        totalattempts=totalattempts,
                        averagescore=average
                        )
                t.save()
            

            return render(request,"maths/result.html",{"score":score})
         #   return HttpResponse('<h3> Good Job! Your Score is {% score %} /10<h3>')
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
        elif category == 2 or category == 5: 
            num1 = form1.randnumdoubledigit()
            num2 = form1.randnumdoubledigit()
        elif category == 3 or category == 6 :
            num1 = form1.randnumsingledigit() * 10
            num2 = form1.randnumsingledigit()
       

        output = ['' for i in range(10)]
        validval = [True for i in range(10)]
        zippedlist = zip(num1, num2, validval, output)
        if operator == '+' :  result = num1+num2 
        else : result = num1-num2
        validval = [True for i in range(10)]
        context={}
        return render(request, "maths/addition.html", {"zippedlist": zippedlist,"operator": operator})

def register(request):
    
    if request.method=="POST" :
        form=RegisterForm(request.POST)
        if form.is_valid():
           form.save()
           username=form.cleaned_data.get("username")
           messages.success(request,f'New User {username} created successfully . Welcome {username}')
         
       #    login(request, username)
#           return redirect("/")
        else:
            for msg in form.error_messages:
                messages.error(request,f' {msg}: {form.error_messages[msg]}')
            return render(request,"maths/register.html",{"form":form})
    form=RegisterForm()
   
    return render(request,"maths/register.html",{"form":form})
