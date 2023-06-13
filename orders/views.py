
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView,CreateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveAPIView
from .models import Order,OrderItem,OrderCheckout
from products.models import Product
from .serializers import OrderSerializer,OrderItemSerializer,OrderCheckoutSerializer
from rest_framework.pagination import PageNumberPagination
from django.db import transaction
from django.db.models import Sum
from django.core.exceptions import BadRequest
from django.shortcuts import get_object_or_404


class OrderListAPIView(ListAPIView):
    queryset = Order.objects.filter().select_related('user')
    serializer_class = OrderSerializer
    pagination_class = PageNumberPagination
    filterset_fields = ['user']

class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.filter()
    serializer_class = OrderSerializer
    pagination_class = PageNumberPagination


class OrderItemCreateAPIView(CreateAPIView):
    queryset = OrderItem.objects.filter().select_related('product')
    serializer_class = OrderItemSerializer
    pagination_class = PageNumberPagination

    
    def perform_create(self, serializer):
        with transaction.atomic():
            order,_ = Order.objects.get_or_create(user=self.request.user,is_completed=False)
            product_id = self.request.data.get('product')
            product = get_object_or_404(Product,id=product_id)
            order_quantity = self.request.data.get('quantity')

            if product.stock_quantity == 0:
                raise BadRequest(f"Product Stock Out")

            elif product.stock_quantity < order_quantity:
                raise BadRequest(f"Available product is {product.stock_quantity}")

            item = serializer.save(order=order)

            item.price = item.quantity * item.product.price
            item.save()
            order_amount = OrderItem.objects.filter(order=order).aggregate(total_amount=Sum('price')).get('total_amount', 0)
            order.total_amount = order_amount
            order.save()





class OrderItemDestroyAPIView(DestroyAPIView):
    queryset = OrderItem.objects.filter()
    serializer_class = OrderItemSerializer


    def perform_destroy(self, instance):
            order = instance.order
            order.total_amount -= instance.price

            
            with transaction.atomic():
                instance.delete()
                order.save()



class OrderCheckoutListCreateAPIView(ListCreateAPIView):
    queryset = OrderCheckout.objects.filter().select_related('order')
    serializer_class = OrderCheckoutSerializer
    filterset_fields = ['user']

    def perform_create(self, serializer):

        user = self.request.user
        order_id = self.request.data.get("order")
        order = get_object_or_404(Order, id=order_id)

        if order.is_completed:
            raise BadRequest("Checkout is completed")

        items = OrderItem.objects.filter(order=order)

        with transaction.atomic():
            serializer.save(user=user)

            for item in items:
                product = item.product
                if product.stock_quantity == 0:
                    raise BadRequest(f"Product Stock Out")

                elif product.stock_quantity < item.quantity:
                    raise BadRequest(f"Available product is {product.stock_quantity}")

               
                product.stock_quantity -= item.quantity
                product.save()

            order.is_completed = True
            order.save()
        

class OrderCheckoutRetrieveAPIView(RetrieveAPIView):
    queryset = OrderCheckout.objects.filter()
    serializer_class = OrderCheckoutSerializer





        

            


        

    