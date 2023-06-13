from django.core.exceptions import ObjectDoesNotExist,BadRequest
from django.http.response import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler 

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response:
        response=response

    elif isinstance(exc, KeyError):
        response= Response({exc.__str__().strip("'"): ["This Field Is Required"]}, status=status.HTTP_400_BAD_REQUEST)
    
    elif isinstance(exc, ObjectDoesNotExist):
        response= Response({'message': exc.__str__()}, status=status.HTTP_404_NOT_FOUND)
    
    else:
        response= Response({'message': exc.__str__()}, status=status.HTTP_400_BAD_REQUEST)

    return response
    