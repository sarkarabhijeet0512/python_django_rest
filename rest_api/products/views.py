from .models import Products, Discount, Product_Inventory, Product_Category
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import productsSerializer


class ProductsList(APIView):
    def get(self, request):
        queryset = Products.objects.all()
        serializer_class = productsSerializer(queryset, many=True)
        return Response({"status": "sucess",
                        "code": status.HTTP_200_OK,
                         "data": serializer_class.data})

    # POST API request processing
    def post(self, request):
        products_data = JSONParser().parse(request)
        # isinstant check if the json passed is list or single object
        many = True if isinstance(products_data, list) else False
        products_serializer = productsSerializer(data=products_data, many=many)
        if products_serializer.is_valid():
            products_serializer.save()
            return Response({"status": "sucess", "code": status.HTTP_201_CREATED, "data": products_serializer.data})
        return Response(products_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductsEdits(APIView):
    # GET API request processing
    def get_object(self, request):
        id = request.query_params["id"]
        try:
            queryset = Products.objects.get(pk=id)
            return productsSerializer(queryset, many=False)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request):
        queryset = self.get_object(request)
        return Response({"status": "sucess",
                         "code": status.HTTP_201_CREATED,
                         "data": queryset.data})

    def put(self, request):
        id = request.query_params["id"]
        queryset = self.get_object(id)
        serializer_class = productsSerializer(
            queryset, request.data, many=False)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        id = request.query_params["id"]
        queryset = self.get_object(id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DiscountList(APIView):
    def get(self, request):
        queryset = Discount.objects.all()
        serializer_class = productsSerializer(queryset, many=True)
        return Response({"status": "sucess",
                        "code": status.HTTP_200_OK,
                         "data": serializer_class.data})

    # POST API request processing
    def post(self, request):
        products_data = JSONParser().parse(request)
        # isinstant check if the json passed is list or single object
        many = True if isinstance(products_data, list) else False
        discounts_serializer = productsSerializer(
            data=products_data, many=many)
        if discounts_serializer.is_valid():
            discounts_serializer.save()
            return Response({"status": "sucess", "code": status.HTTP_201_CREATED, "data": discounts_serializer.data})
        return Response(discounts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DiscountEdits(APIView):
    # GET API request processing
    def get_object(self, request):
        id = request.query_params["id"]
        try:
            queryset = Discount.objects.get(pk=id)
            return productsSerializer(queryset, many=False)
        except Discount.DoesNotExist:
            raise Http404

    def get(self, request):
        queryset = self.get_object(request)
        return Response({"status": "sucess",
                         "code": status.HTTP_201_CREATED,
                         "data": queryset.data})

    def put(self, request):
        id = request.query_params["id"]
        queryset = self.get_object(id)
        serializer_class = productsSerializer(
            queryset, request.data, many=False)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        id = request.query_params["id"]
        queryset = self.get_object(id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Product_Category_List(APIView):
    def get(self, request):
        queryset = Product_Category.objects.all()
        serializer_class = productsSerializer(queryset, many=True)
        return Response({"status": "sucess",
                        "code": status.HTTP_200_OK,
                         "data": serializer_class.data})

    # POST API request processing
    def post(self, request):
        products_category_data = JSONParser().parse(request)
        # isinstant check if the json passed is list or single object
        many = True if isinstance(products_category_data, list) else False
        products_category_serializer = productsSerializer(
            data=products_category_data, many=many)
        if products_category_serializer.is_valid():
            products_category_serializer.save()
            return Response({"status": "sucess", "code": status.HTTP_201_CREATED, "data": products_category_serializer.data})
        return Response(products_category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Product_Category_Edits(APIView):
    # GET API request processing
    def get_object(self, request):
        id = request.query_params["id"]
        try:
            queryset = Product_Category.objects.get(pk=id)
            return productsSerializer(queryset, many=False)
        except Discount.DoesNotExist:
            raise Http404

    def get(self, request):
        queryset = self.get_object(request)
        return Response({"status": "sucess",
                         "code": status.HTTP_201_CREATED,
                         "data": queryset.data})

    def put(self, request):
        id = request.query_params["id"]
        queryset = self.get_object(id)
        serializer_class = productsSerializer(
            queryset, request.data, many=False)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        id = request.query_params["id"]
        queryset = self.get_object(id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Product_Inventory_List(APIView):
    def get(self, request):
        queryset = Product_Inventory.objects.all()
        serializer_class = productsSerializer(queryset, many=True)
        return Response({"status": "sucess",
                        "code": status.HTTP_200_OK,
                         "data": serializer_class.data})

    # POST API request processing
    def post(self, request):
        products_inventory_data = JSONParser().parse(request)
        # isinstant check if the json passed is list or single object
        many = True if isinstance(products_inventory_data, list) else False
        products_inventory_serializer = productsSerializer(
            data=products_inventory_data, many=many)
        if products_inventory_serializer.is_valid():
            products_inventory_serializer.save()
            return Response({"status": "sucess", "code": status.HTTP_201_CREATED, "data": products_inventory_serializer.data})
        return Response(products_inventory_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Product_Inventory_Edits(APIView):
    # GET API request processing
    def get_object(self, request):
        id = request.query_params["id"]
        try:
            queryset = Product_Inventory.objects.get(pk=id)
            return productsSerializer(queryset, many=False)
        except Discount.DoesNotExist:
            raise Http404

    def get(self, request):
        queryset = self.get_object(request)
        return Response({"status": "sucess",
                         "code": status.HTTP_201_CREATED,
                         "data": queryset.data})

    def put(self, request):
        id = request.query_params["id"]
        queryset = self.get_object(id)
        serializer_class = productsSerializer(
            queryset, request.data, many=False)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        id = request.query_params["id"]
        queryset = self.get_object(id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
