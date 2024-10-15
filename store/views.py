from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product


# views.py
#Отображение списка продуктов
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


#Отображение деталей продукта
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


#Создание продукта
class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'description', 'price', 'image', 'category']
    success_url = reverse_lazy('product_list')


#обновление продукта
class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'description', 'price', 'image', 'category']
    success_url = reverse_lazy('product_list')


#удаление продукта
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

