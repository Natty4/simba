from django.urls import path

from order.views import checkout, OrdersList

urlpatterns = [
    path('checkout/', checkout, name = 'checkout'),
    path('orders/', OrdersList.as_view(), name = 'my_orders'),  
]