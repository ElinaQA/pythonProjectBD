from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django_filters.views import FilterView
from .models import Product
from .filters import ProductFilter
from django.shortcuts import render

from store import filters


def product_list(request):
    filter = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'store/product_list.html', {'filter': filter})

# views.py
#Отображение списка продуктов
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'filter'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset  # Передаем фильтр в контекст
        return context


#Отображение деталей продукта
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    #def get_queryset(self):
     #   queryset = super().get_queryset()
     #   self.filterset = ProductFilter(self.request.GET, queryset=queryset)
     #   return self.filterset.qs


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

