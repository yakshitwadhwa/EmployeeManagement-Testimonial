from django.contrib import admin
from django.urls import path,include
from .views import *



urlpatterns = [
    path("",emp_home),
    path("add/",add_emp),
    path("delete/<int:emp_id>",delete),
    path("update/<int:emp_id>",update),
    # path("doupdate/",doupdate),
    path("testimonials",testimonials),
    path('doupdate/<int:emp_id>/', doupdate, name='doupdate'),




]
