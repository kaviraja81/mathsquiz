from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import numpy as np


class AdditionForm():

    def randnum(self):
        number1=np.random.randint(0,10,10)
        return number1
    # class Meta:
    #     model=User
    #     fields=["number1","username","password1"]