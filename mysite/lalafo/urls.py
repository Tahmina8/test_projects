from .views import ProductListview, CategoryListview, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from django.urls import path



urlpatterns = [
    path('', ProductListview.as_view(), name='product_list'),
    path('category/', CategoryListview.as_view(), name='category_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete')
]
