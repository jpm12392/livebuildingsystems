from rest_framework.response import Response
from rest_framework import generics, status, permissions
from .serailizers import *


## Meters APIView List.
class MeterAPIView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MeterSerailzier

    def get(self, request, *args, **kwargs):
        try:
            meters = Meter.objects.all().order_by('-id')
            serializer = self.serializer_class(meters, many=True)
            context = {'status': True,'message': 'Meter found successfully.', 'data': serializer.data}
            return Response(context, status=status.HTTP_200_OK)
        except Exception as e:
            context = {'status': False, 'message': 'Something Went Wrong'}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                context = {'status': True,'message': 'Meter added successfully.'}
            else:
                context = {'status': False,'message': serializer.errors}
            return Response(context, status=status.HTTP_200_OK)

        except Exception as e:
            context = {'status': False, 'message': 'Something Went Wrong'}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



## Meter Details .
class MeterDetailAPIView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MeterDataSerailzier

    def get(self, request, meter_id, format=None):
        try:
            if meter_id:
                meterdata = MeterData.objects.filter(meter=meter_id).order_by('-timestamp')
                serializer = self.serializer_class(meterdata, many=True)
                context = {'status': True,'message': 'Meter found successfully.', 'data': serializer.data}
            else:
                context = {'status': False,'message': 'Please enter meter id.'}
            return Response(context, status=status.HTTP_200_OK)
        except Exception as e:
            context = {'status': False, 'message': 'Something Went Wrong'}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



## Meter Data APIView List.
class MeterDataAPIView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MeterDataSerailzier

    def get(self, request, *args, **kwargs):
        try:
            meters = MeterData.objects.all().order_by('-timestamp')
            serializer = self.serializer_class(meters, many=True)
            context = {'status': True,'message': 'Meter Data found successfully.', 'data': serializer.data}
            return Response(context, status=status.HTTP_200_OK)
        except Exception as e:
            context = {'status': False, 'message': 'Something Went Wrong'}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                context = {'status': True,'message': 'Meter Data added successfully.'}
            else:
                context = {'status': False,'message': serializer.errors}
            return Response(context, status=status.HTTP_200_OK)

        except Exception as e:
            context = {'status': False, 'message': 'Something Went Wrong'}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
