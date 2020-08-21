from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import numpy as np


class AdditionForm():

    def randnumsingledigit(self):
        number=np.random.randint(0,10,10)
        return number
    
    def randnumdoubledigit(self):
        number=np.random.randint(10,100,10)
        return number
    # class Meta:
    #     model=User
    #     fields=["number1","username","password1"]

class RegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=["username","password1","password2","email"]