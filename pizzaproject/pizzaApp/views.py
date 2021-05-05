from django.shortcuts import render
from pizzaproject.constants_variables import requestMethod,statusCodes
import json
from django.http import JsonResponse
from.models import pizzaDropdown

# Create your views here.
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



    

    