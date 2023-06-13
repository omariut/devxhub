
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Product,ProductReview
from .serializers import ProductSerializer,ProductReviewSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db import transaction
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)
    http_method_names = ('patch','get','delete')

class ProductReviewListCreateAPIView(ListCreateAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer

    def perform_create(self, serializer):
        with transaction.atomic():
            review = serializer.save()
            product = review.product
            total_rating = product.rating * product.total_reviews
            product.total_reviews +=1
            product.rating = (total_rating+review.rating)/product.total_reviews
            product.save()



            


class ProductReviewUpdateRetrieveDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer

    def perform_update(self, serializer):
        with transaction.atomic():
            review = serializer.save()
            product = review.product
            total_rating = product.rating * product.total_reviews
            product.total_reviews +=1
            product.rating = (total_rating+review.rating)/product.total_reviews
            product.save()
