from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS



class ProductListView(ListAPIView):
    queryset = Product.objects.prefetch_related('color','size').all()
    serializer_class = ProductSerializer


class ProdactByCategoryView(ListAPIView):
    def get(self ,request , category = None , format = None):
        
        product = Product.objects.filter(category__name = category)
        serialized_product = ProductSerializer(product, many = True)
        if serialized_product.data:
            Status = status.HTTP_200_OK
        else :
            Status = status.HTTP_404_NOT_FOUND
        return Response({
            "Products" : serialized_product.data, 'status' : Status
            })

class ProductDetailView(APIView):
    
    def get(self ,request , pk = None , format = None):

       
        
        product = Product.objects.get(id = pk)
        images = Image.objects.filter(product = pk)
        reviews = Review.objects.filter(product = pk)

        ##serializing product, color, size and images
        serialized_product = ProductSerializer(product)
        serialized_images = ImageSerializer(images , many = True)
        serialized_reviews = ReviewSerializer(reviews , many = True)

        if serialized_product.data:
            Status = status.HTTP_200_OK
        else :
            Status = status.HTTP_404_NOT_FOUND
        return Response({
            "Product-Info" : serialized_product.data,
            "Product-Images" : serialized_images.data, 
            "Product-Reviews" : serialized_reviews.data,
            "status" : Status,
        })


class ReviewsListView(ListAPIView):
    queryset = Review.objects.prefetch_related('product', 'user').all()
    serializer_class = ReviewSerializer

class ReviewCreateView(APIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated|IsOwnerOrReadOnly]
    def post(self, request, *args, **kwargs):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):

            serializer.save()       
            return Response({
                'data' : serializer.data, 
                'status': status.HTTP_201_CREATED
                })
        else:
            return Response({ 
                'msg' : 'invalid data', 
                'status' : status.HTTP_400_BAD_REQUEST 
                })

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CastegorySerializer





