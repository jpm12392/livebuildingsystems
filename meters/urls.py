from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/meters/', MeterAPIView.as_view(), name='meters'),
    path('api/v1/meters/<int:meter_id>', MeterDetailAPIView.as_view(), name='meters_details'),
    path('api/v1/meter_data/', MeterDataAPIView.as_view(), name='meter_data'),
   
    
]