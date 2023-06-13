from django.db import models
from django.contrib.auth.models import User
from products.models import Product
import uuid



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.pk} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['order', 'product'], name='unique_order_product')
        ]

    def __str__(self):
        return f"OrderItem: {self.product.name} ({self.quantity})"





class OrderCheckout(models.Model):

    PAYMENT_METHOD_CHOICES = (
        ('online', 'Online'),
        ('cash_on_delivery', 'Cash on Delivery'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"Order Checkout - {self.order.id} ({self.user.username})"

