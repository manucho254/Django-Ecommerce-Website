from django.urls import path
from .views import (
     become_vendor,vendor_dashboard, 
     add_product, edit_vendor,
     vendor_products
     )

urlpatterns = [
    path('vendor/signup', become_vendor, name="become-vendor"),
    path('vendor/dashboard/', vendor_dashboard, name="vendor-dashboard"),
    path('vendor/edit/', edit_vendor, name="vendor-edit"),
    path('vendor/dashboard/add', add_product , name='add_product'),
    path('<int:vendor_id>/', vendor_products, name="vendor-products")

]
