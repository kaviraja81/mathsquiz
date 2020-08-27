from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path("register/",views.register,name="register"),
    path('', include("django.contrib.auth.urls")),
    path('grade1/',views.grade,name="grade"),
    path('grade2/',views.grade,name="grade"),
    path("grade1/add/<int:category>/",views.add,name="add"),
    path("grade1/sub/<int:category>/",views.add,name="add"),
    path("grade2/add/<int:category>/",views.add,name="add"),
    path("grade2/sub/<int:category>/",views.add,name="add")
]