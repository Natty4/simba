from django.urls import path

from order.views import OrdersList, Checkout #checkout,

urlpatterns = [
    path('checkout', Checkout.as_view(), name = 'checkout'),
    path('orders/', OrdersList.as_view(), name = 'my_orders'),  
]