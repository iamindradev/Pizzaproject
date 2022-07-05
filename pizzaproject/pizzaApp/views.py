from django.shortcuts import render
from pizzaproject.constants_variables import requestMethod,statusCodes
import json
from django.http import HttpResponse, JsonResponse
from.models import pizzaDropdown, pizzaCreated

#JSON REQUIRED
# {
#     "pid":"0",
#     "feild":"PIZZAPARAMETER",
#     "value":"TYPE"
# }
#AND FOR DEFINING VALUES OF TYPE
# {
#     "pid":4,it can ab anything as created in first row
#     "feild":"TYPE",
#     "value":"SQUARE"
# }
#this function can also be used for creating or adding new type,size and toppings for pizza
def Helloworld(request):
    return HttpResponse("Hello World")
def createPizzaparameter(request):
    if requestMethod.GET_REQUEST(request):
        if request.GET['request_type']=='getParameter':
            response_values = list(pizzaDropdown.objects.filter(feild='PIZZAPARAMETER').values('sno','feild','value'))
            if len(response_values)>0:
                return JsonResponse(response_values,safe= False)
            else:
                response_values=statusCodes.STATUS_BAD_REQUEST                      
    if requestMethod.POST_REQUEST(request):
        data= json.loads(request.body)
        pizzaDropdown.objects.create(**data)
        response_values={'msg':'CREATED'}
    else:
        response_values=statusCodes.STATUS_METHOD_NOT_ALLOWED
    return JsonResponse(response_values,safe= False)


#this function is created for dropdown to user for the size,type,toppings he can chose for his pizza.  
def getParameter(request):
    if requestMethod.GET_REQUEST(request):
        if request.GET['request_type']=='getSize':
            key = 'SIZE'
        elif request.GET['request_type']=='getType':
            key = 'TYPE'
        elif request.GET['request_type']=='getToppings':
            key='TOPPINGS'
        else:
            response_values=statusCodes.STATUS_BAD_REQUEST
        print(key)
        response_values = list(pizzaDropdown.objects.filter(feild=key).values('sno','feild','value'))
        if len(response_values)>0:
            return JsonResponse(response_values,safe= False)
        else:
            response_values=statusCodes.STATUS_BAD_REQUEST 
    return JsonResponse(response_values,safe= False)


#this fuction is used to create the create the pizza of his choice from dropdown 
#JSON BY GETTING ID FROM DROPDOWN
# {
#     "size":11,
#     "type":6,
#     "toppings":17
# }
def createPizza(request):
    if requestMethod.POST_REQUEST(request):
        data= json.loads(request.body)
        pizzaCreated.objects.create(type=pizzaDropdown.objects.get(sno=data['type']),size=pizzaDropdown.objects.get(sno=data['size']),toppings=pizzaDropdown.objects.get(sno=data['toppings']))
        response_values={'msg':'CREATED'}
    else:
        response_values=statusCodes.STATUS_METHOD_NOT_ALLOWED
    return JsonResponse(response_values,safe= False)


#this function is used for creating the list of combination of pizza that alrady created/orderd.
def pizzaAlreadyCreated(request):
    if requestMethod.GET_REQUEST(request):
        response_values=list(pizzaCreated.objects.all().values('id','size','size__value','type','type__value','toppings','toppings__value'))
    else:
        response_values=statusCodes.STATUS_METHOD_NOT_ALLOWED
    return JsonResponse(response_values,safe= False)


#this function is used to edit the size or toppings of pizza already created
#JSON FOR UPDATE
# {
#     "id": 1,
#     "size":10,
#     "type":5,
#     "toppings":16
# }
def pizzaEdit(request):
    if requestMethod.POST_REQUEST(request):
        data= json.loads(request.body)
        # for checking if combination already exists or not
        if pizzaCreated.objects.filter(type=data['type'],size=data['size'],toppings=data['toppings']).exists():
            response_values={'msg':'THE COMBINATION YOU CREATING ALREADY EXISTS'}#we can also rediret to already exist list
        else:
            pizzaCreated.objects.filter(id=data['id']).update(type=pizzaDropdown.objects.get(sno=data['type']),size=pizzaDropdown.objects.get(sno=data['size']),toppings=pizzaDropdown.objects.get(sno=data['toppings']))
            response_values={'msg':'PIZZA OF YOUR CHOICE UPDATED'}
    else:
        response_values=statusCodes.STATUS_METHOD_NOT_ALLOWED
    return JsonResponse(response_values,safe= False)

    

    