from rest_framework import serializers
from .models import *


## Meter Serailzier
class MeterSerailzier(serializers.ModelSerializer):
    class Meta:
        model = Meter
        fields = '__all__'


## Meter Data Serailzier
class MeterDataSerailzier(serializers.ModelSerializer):
    class Meta:
        model = MeterData
        fields = '__all__'