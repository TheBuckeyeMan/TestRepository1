from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.



class PersonalDataView(APIView):
    serializer_class = PersonalDataSerializer
    def get(self,request):
        output = [{
            'id': output.id, 
            'firstname': output.firstname,
            'lastname': output.lastname,
            'age': output.age,
            'height': output.height,
        } for output in PersonalData.objects.all()]
        return Response(output)
    def post(self,request):
        serializer = PersonalDataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        












