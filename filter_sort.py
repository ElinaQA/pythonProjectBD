import os
import django

# Укажите путь к settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_store.settings')
django.setup()

from store.models import  Product

# Продукты с ценой больше 20
expensive_products = Product.objects.filter(price__gt=20)
for product in expensive_products:
    print(product.name)

# Продукты с названием, содержащим 'Книга'
books = Product.objects.filter(name__icontains='Книга')
for product in books:
    print(product.name)

# Продукты, созданные в категории 'Электроника'
electronics = Product.objects.filter(category__name='Электроника')
for product in electronics:
    print(product.name)

# Продукты, цена которых не равна 299.99
non_expensive_products = Product.objects.exclude(price=299.99)
for product in non_expensive_products:
    print(product.name)

# Продукты, название которых не содержит 'Футболка'
non_shirts = Product.objects.exclude(name__icontains='Футболка')
for product in non_shirts:
    print(product.name)

# Продукты, которые не находятся в категории 'Книги'
not_books = Product.objects.exclude(category__name='Книги')
for product in not_books:
    print(product.name)
# Продукты по возрастанию цены
products_sorted_by_price = Product.objects.all().order_by('price')
for product in products_sorted_by_price:
    print(product.name, product.price)

# Продукты по убыванию цены
products_sorted_by_price_desc = Product.objects.all().order_by('-price')
for product in products_sorted_by_price_desc:
    print(product.name, product.price)

# Продукты, отсортированные по названию
products_sorted_by_name = Product.objects.all().order_by('name')
for product in products_sorted_by_name:
    print(product.name)


