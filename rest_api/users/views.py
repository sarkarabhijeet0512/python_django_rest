# from django.shortcuts import render
from users.models import Users
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import UsersSerializer
from django.contrib.auth.hashers import make_password
# from rest_framework.decorators import api_view


class UserList(APIView):
    def get(self, request):
        queryset = Users.objects.all()
        serializer_class = UsersSerializer(queryset, many=True)
        return Response({"status": "sucess",
                        "code": status.HTTP_201_CREATED,
                         "data": serializer_class.data})

    # POST API request processing
    def post(self, request):
        users_data = JSONParser().parse(request)
        users_data['password'] = make_password(users_data['password'])
        # isinstant check if the json passed is list or single object
        many = True if isinstance(users_data, list) else False
        users_serializer = UsersSerializer(data=users_data, many=many)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response({"status": "sucess", "code": status.HTTP_201_CREATED, "data": users_serializer.data})
        return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class usersEdits(APIView):
    # GET API request processing
    def get_object(self, request):
        id = request.query_params["id"]
        try:
            queryset = Users.objects.get(pk=id)
            return UsersSerializer(queryset, many=False)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request):
        queryset = self.get_object(request)
        return Response({"status": "sucess",
                         "code": status.HTTP_201_CREATED,
                         "data": queryset.data})

    def put(self, request):
        id = request.query_params["id"]
        queryset = self.get_object(id)
        serializer_class = UsersSerializer(queryset, request.data, many=False)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        id = request.query_params["id"]
        queryset = self.get_object(id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
