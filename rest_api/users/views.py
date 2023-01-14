from django.shortcuts import render
from users.models import Users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status


from .serializers import UsersSerializer

from rest_framework.decorators import api_view


class usersList(APIView):
    # GET API request processing
    def get(self, request):
        try:
            id = request.query_params["id"]
            queryset = Users.objects.get(
                pk=int(id))
            serializer_class = UsersSerializer(queryset, many=False)
            return Response(serializer_class.data)
        except:
            queryset = Users.objects.all()
            serializer_class = UsersSerializer(queryset, many=True)
            return Response(serializer_class.data)
    # POST API request processing

    def post(self, request):
        users_data = JSONParser().parse(request)
        # isinstant check if the json passed is list or single object
        many = True if isinstance(request.data, list) else False
        users_serializer = UsersSerializer(data=users_data, many=many)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data, status=status.HTTP_201_CREATED)
        return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        users_data = JSONParser().parse(request)
        # isinstant checks if the json passed is list or single object
        many = True if isinstance(request.data, list) else False
        users_serializer = UsersSerializer(data=users_data, many=many)
        if users_serializer.is_valid():
            try:
                id = request.query_params["id"]
                queryset = Users.objects.get(
                    pk=int(id))
                serializer_class = UsersSerializer(queryset, many=False)
                return Response(serializer_class.data)
            except:
                queryset = Users.objects.all()
                serializer_class = UsersSerializer(queryset, many=True)
                return Response(serializer_class.data)
