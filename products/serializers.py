from rest_framework import serializers
from .models import Product,ProductReview
from django.contrib.auth.models import User
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset = User.objects.filter()  # Set the current user as the default value
    )

    class Meta:
        model = ProductReview
        fields = ['id', 'user', 'product', 'content', 'rating', 'created_at']
        read_only_fields = ['id', 'created_at']
