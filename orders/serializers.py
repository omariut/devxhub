from rest_framework import serializers
from .models import Order, OrderItem,OrderCheckout

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id','product', 'quantity','price')
        read_only_fields = ('price','order')
       

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'order_date', 'total_amount', 'items','is_completed')
   

        
class OrderCheckoutSerializer(serializers.ModelSerializer):
    order_detail = OrderSerializer(read_only=True,source='order')
    price = serializers.FloatField(source='order.price', read_only=True)
    
    class Meta:
        model = OrderCheckout
        fields = '__all__'
        read_only_fields = ("user",'price',"order_detail")
        write_only_fields = ("order",)

   