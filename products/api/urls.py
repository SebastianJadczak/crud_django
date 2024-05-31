from django.urls import path

from products import views

urlpatterns = [
    path('', views.ProductsListView.as_view(), name='products-list'),
    path('add/', views.ProductCreateView.as_view(), name='product-create'),
    path('category/<int:pk>/', views.ProductsInCategoryListView.as_view(), name='products-list'),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='product-update'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product-delete'),
]
