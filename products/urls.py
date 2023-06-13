from django.urls import path
from .views import ProductListCreateAPIView,ProductRetrieveUpdateDestroyAPIView,ProductReviewListCreateAPIView,ProductReviewUpdateRetrieveDestroyAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update'),
    path('product-reviews/', ProductReviewListCreateAPIView.as_view(), name='product-review-list-create'),
    path('product-reviews/<int:pk>/', ProductReviewUpdateRetrieveDestroyAPIView.as_view(), name='product-review-detail'),
]
