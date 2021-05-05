from django.urls import path
from .views import createPizzaparameter,getParameter,createPizza,pizzaAlreadyCreated,pizzaEdit#here we also can use * but it creates ambiguity when we use more apps and views

urlpatterns = [
    path('CreatePizzaparameter/',createPizzaparameter),#for creating paramters for pizza 
    path('getParameter/',getParameter),#for getting the predefined parameters
    path('createPizza/',createPizza),#for creating pizza of your wish and(size,type,toppings)
    path('pizzaAlreadycreated/',pizzaAlreadyCreated),#for getting the list of combination of pzza already created
    path('pizzaEdit/',pizzaEdit)# for editng pizza alredy created

]
