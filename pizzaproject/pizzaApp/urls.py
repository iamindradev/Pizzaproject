from django.urls import path
from .views import createPizzaparameter,getParameter

urlpatterns = [
    path('CreatePizzaparameter/',createPizzaparameter),#for creating pizza 
    path('getParameter/',getParameter)#for getting the predefined parameters

]
