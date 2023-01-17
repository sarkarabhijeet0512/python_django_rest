# from django.shortcuts import render

from .models import payments
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import paymentsSerializer
# Create your views here.


class payments_list(APIView):
    def get(self, request):
        queryset = payments.objects.all()
        serializer_class = paymentsSerializer(queryset, many=True)
        return Response({"status": "sucess",
                        "code": status.HTTP_200_OK,
                         "data": serializer_class.data})

    # POST API request processing
    def post(self, request):
        products_data = JSONParser().parse(request)
        # isinstant check if the json passed is list or single object
        many = True if isinstance(products_data, list) else False
        payments_serializer = paymentsSerializer(data=products_data, many=many)
        if payments_serializer.is_valid():
            payments_serializer.save()
            return Response({"status": "sucess", "code": status.HTTP_201_CREATED, "data": payments_serializer.data})
        return Response(payments_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class paymentsEdits(APIView):
    # GET API request processing
    def get_object(self, request):
        id = request.query_params["id"]
        try:
            queryset = payments.objects.get(pk=id)
            return paymentsSerializer(queryset, many=False)
        except payments.DoesNotExist:
            raise Http404

    def get(self, request):
        queryset = self.get_object(request)
        return Response({"status": "sucess",
                         "code": status.HTTP_201_CREATED,
                         "data": queryset.data})

    def put(self, request):
        id = request.query_params["id"]
        queryset = self.get_object(id)
        payments_serializer = paymentsSerializer(
            queryset, request.data, many=False)
        if payments_serializer.is_valid():
            payments_serializer.save()
            return Response(payments_serializer.data)
        return Response(payments_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        id = request.query_params["id"]
        queryset = self.get_object(id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
