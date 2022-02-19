from .models import *
from rest_framework import serializers
from users.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ["id"] 

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        exclude = ["id"]  

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        exclude = ["id"]  


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    color = ColorSerializer(many=True, read_only=True)
    size = SizeSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('name',
                            'brand',
                            'category',
                            'short_description',
                            'unit_price',
                            'discount_price',
                            'status',
                            'available_quantity',
                            'thumbnail',
                            'color',
                            'size',
                            'features',
                            'created',
                            'updated',)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ["id" , "product"]

class ReviewSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Review

        exclude = ["id",]
        