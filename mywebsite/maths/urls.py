from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path("grade1/add/<int:category>/",views.add,name="add3"),
    path("register/",views.register,name="register"),
    path('', include("django.contrib.auth.urls")),
    path('grade1/',views.grade1,name="grade1"),
    path("grade1/add2digit/<int:category>/",views.add,name="add3"),
]