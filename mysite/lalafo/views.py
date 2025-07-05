from .models import Product, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProductForms
from django.urls import reverse_lazy





class ProductListview(ListView):
    queryset = Product.objects.all()
    template_name = 'product_list.html'
    context_object_name = 'products'

class CategoryListview(ListView):
    queryset = Category.objects.all()
    template_name = 'category_list.html'
    context_object_name = 'categories'

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    form_class = ProductForms
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    queryset = Product.objects.all()
    template_name = 'product_update.html'
    form_class = ProductForms
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    queryset = Product.objects.all()
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')