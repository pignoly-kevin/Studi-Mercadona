from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_promotion/<int:product_id>/', views.add_promotion, name='add_promotion'),
]