from django.urls import path
from .views import OrderListAPIView,OrderItemCreateAPIView,OrderRetrieveUpdateDestroyAPIView,OrderItemDestroyAPIView,OrderCheckoutListCreateAPIView,OrderCheckoutRetrieveAPIView

urlpatterns = [
    path('orders/', OrderListAPIView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-retrieve-update'),
    path('order-items/', OrderItemCreateAPIView.as_view(), name='order-item-list-create'),
    path('order-items/<int:pk>/', OrderItemDestroyAPIView.as_view(), name='order-item-delete'),
    path('order-checkouts/', OrderCheckoutListCreateAPIView.as_view(), name='order-checkout-list-create'),
    path('order-checkouts/<int:pk>/', OrderCheckoutRetrieveAPIView.as_view(), name='order-checkout-single'),
]
