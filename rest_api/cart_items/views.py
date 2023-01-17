# Create your views here.
# from django.shortcuts import render

from .models import cart_items
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import cartSerializer
# Create your views here.


class cart_items_list(APIView):
    # GET API request processing
    def get(self, request):
        queryset = cart_items.objects.all()
        serializer_class = cartSerializer(queryset, many=True)
        return Response({"status": "sucess",
                        "code": status.HTTP_200_OK,
                         "data": serializer_class.data})

    # POST API request processing
    def post(self, request):
        products_data = JSONParser().parse(request)
        # isinstant check if the json passed is list or single object
        many = True if isinstance(products_data, list) else False
        cart_items_serializer = cartSerializer(data=products_data, many=many)
        if cart_items_serializer.is_valid():
            cart_items_serializer.save()
            return Response({"status": "sucess", "code": status.HTTP_201_CREATED, "data": cart_items_serializer.data})
        return Response(cart_items_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class cart_items_Edits(APIView):
    # GET API request processing
    def get_object(self, request):
        id = request.query_params["id"]
        try:
            queryset = cart_items.objects.get(pk=id)
            return cartSerializer(queryset, many=False)
        except cart_items.DoesNotExist:
            raise Http404

    def get(self, request):
        queryset = self.get_object(request)
        return Response({"status": "sucess",
                         "code": status.HTTP_201_CREATED,
                         "data": queryset.data})

    def put(self, request):
        id = request.query_params["id"]
        queryset = self.get_object(id)
        cart_items_serializer = cartSerializer(
            queryset, request.data, many=False)
        if cart_items_serializer.is_valid():
            cart_items_serializer.save()
            return Response(cart_items_serializer.data)
        return Response(cart_items_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        id = request.query_params["id"]
        queryset = self.get_object(id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
