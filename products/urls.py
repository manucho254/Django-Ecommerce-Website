from django.urls import path
from .views import ProductDetailView,CategoryView


urlpatterns = [
    path("<slug:category_slug>/<slug:product_slug>/", ProductDetailView, name="product-detail"),
    path("<slug:category_slug>/", CategoryView, name="category")
]
