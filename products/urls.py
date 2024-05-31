from django.contrib import admin
from django.urls import path, include

app_name = 'products'

urlpatterns = [
    path('api/', include('products.api.urls')),
]
