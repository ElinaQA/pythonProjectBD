import django_filters
from .models import Product, Category

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Название продукта')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), label='Категория')
    price = django_filters.RangeFilter(label='Цена (от-до)')
    available = django_filters.BooleanFilter(method='filter_available', label='В наличии')

    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'available']

    def filter_available(self, queryset, name, value):
        if value:
            return queryset.filter(storage_amount__gt=0)
        return queryset.filter(storage_amount=0)
