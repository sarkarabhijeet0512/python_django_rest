from django.shortcuts import render
from .models import order_details, order_items
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import OrdersSerializer


class order_details_list(APIView):
    def get(self, request):
        queryset = order_details.objects.all()
        serializer_class = OrdersSerializer(queryset, many=True)
        return Response({"status": "sucess",
                        "code": status.HTTP_200_OK,
                         "data": serializer_class.data})

    # POST API request processing
    def post(self, request):
        order_details_data = JSONParser().parse(request)
        # isinstant check if the json passed is list or single object
        many = True if isinstance(order_details_data, list) else False
        order_details_serializer = OrdersSerializer(
            data=order_details_data, many=many)
        if order_details_serializer.is_valid():
            order_details_serializer.save()
            return Response({"status": "sucess", "code": status.HTTP_201_CREATED, "data": order_details_serializer.data})
        return Response(order_details_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class order_details_Edits(APIView):
    # GET API request processing
    def get_object(self, request):
        id = request.query_params["id"]
        try:
            queryset = order_details.objects.get(pk=id)
            return OrdersSerializer(queryset, many=False)
        except order_details.DoesNotExist:
            raise Http404

    def get(self, request):
        queryset = self.get_object(request)
        return Response({"status": "sucess",
                         "code": status.HTTP_201_CREATED,
                         "data": queryset.data})

    def put(self, request):
        id = request.query_params["id"]
        queryset = self.get_object(id)
        order_details_serializer = OrdersSerializer(
            queryset, request.data, many=False)
        if order_details_serializer.is_valid():
            order_details_serializer.save()
            return Response(order_details_serializer.data)
        return Response(order_details_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        id = request.query_params["id"]
        queryset = self.get_object(id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class order_items_list(APIView):
    def get(self, request):
        queryset = order_items.objects.all()
        serializer_class = OrdersSerializer(queryset, many=True)
        return Response({"status": "sucess",
                        "code": status.HTTP_200_OK,
                         "data": serializer_class.data})

    # POST API request processing
    def post(self, request):
        order_items_data = JSONParser().parse(request)
        # isinstant check if the json passed is list or single object
        many = True if isinstance(order_items_data, list) else False
        order_items_serializer = OrdersSerializer(
            data=order_items_data, many=many)
        if order_items_serializer.is_valid():
            order_items_serializer.save()
            return Response({"status": "sucess", "code": status.HTTP_201_CREATED, "data": order_items_serializer.data})
        return Response(order_items_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class order_items_Edits(APIView):
    # GET API request processing
    def get_object(self, request):
        id = request.query_params["id"]
        try:
            queryset = order_items.objects.get(pk=id)
            return OrdersSerializer(queryset, many=False)
        except order_items.DoesNotExist:
            raise Http404

    def get(self, request):
        queryset = self.get_object(request)
        return Response({"status": "sucess",
                         "code": status.HTTP_201_CREATED,
                         "data": queryset.data})

    def put(self, request):
        id = request.query_params["id"]
        queryset = self.get_object(id)
        order_items_serializer = OrdersSerializer(
            queryset, request.data, many=False)
        if order_items_serializer.is_valid():
            order_items_serializer.save()
            return Response(order_items_serializer.data)
        return Response(order_items_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        id = request.query_params["id"]
        queryset = self.get_object(id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
