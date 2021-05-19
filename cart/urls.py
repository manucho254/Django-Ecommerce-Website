from django.urls import path
from .views import cartview,SuccesView

urlpatterns = [
    path('', cartview, name='cart'),
    path('success/', SuccesView, name='success')
]