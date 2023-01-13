from employees.models import employees
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import employeesSerializer


class employeeList(APIView):
    def get(self, request):
        queryset = employees.objects.all()
        serializer_class = employeesSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
