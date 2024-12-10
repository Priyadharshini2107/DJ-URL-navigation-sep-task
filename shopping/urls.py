from django.urls import path
from shopping.views import *
app_name='shopping'

urlpatterns=[
    path('suites/',suites,name='suites'),
]