from django.db.models import Q
from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework import status
from users.permissions import IsOwnerOrReadOnly
from .serializers import *
from .models import *



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
    serializer_class = CategorySerializer



@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(short_description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})



# class ImageView(APIView):
    
#     parser_classes = (MultiPartParser, FormParser)


#     def modify_input_for_multiple_files(product, image):
#       dict = {}
#       dict['product'] = product
#       dict['image'] = image
#       return dict

#     def get(self, request):
#         all_images = Image.objects.all()
#         serializer = ImageSerializer(all_images, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     def post(self, request, *args, **kwargs):
#         product = request.data['product']

#         # converts querydict to original dict
#         images = dict((request.data).lists())['image']
#         flag = 1
#         arr = []
#         for img_name in images:
#             modified_data = modify_input_for_multiple_files(product, img_name)
#             file_serializer = ImageSerializer(data=modified_data)
#             if file_serializer.is_valid():
#                 file_serializer.save()
#                 arr.append(file_serializer.data)
#             else:
#                 flag = 0

#         if flag == 1:
#             return Response(arr, status=status.HTTP_201_CREATED)
#         else:
#             return Response(arr, status=status.HTTP_400_BAD_REQUEST)