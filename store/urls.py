from django.urls import path 
from .views import *

urlpatterns = [

    path('' , ProductListView.as_view(), name = 'product_list'),
    path('collections/<str:category>' , ProdactByCategoryView.as_view(), name = 'product_list_by_category'),
    path('product/<int:pk>' , ProductDetailView.as_view() , name = "product_detail"),
    path('product/search/', search, name = 'search_item'),
    path('reviews' , ReviewsListView.as_view() , name = "review_list"),
    path('reviews/create' , ReviewCreateView.as_view() , name = "review_create"),
    path('categorys' , CategoryListView.as_view() , name = "category_list"),

]
