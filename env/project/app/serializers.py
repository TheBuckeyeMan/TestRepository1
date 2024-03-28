from .models import *
from rest_framework import serializers


class PersonalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalData
        fields = ['firstname','lastname','age','height']
