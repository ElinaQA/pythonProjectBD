import os
import django

# Укажите путь к settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_store.settings')
django.setup()

from store.models import Product
from django.db.models import Q

# Продукты с ценой больше 20 или с названием 'Книга'
products_q = Product.objects.filter(Q(price__gt=20) | Q(name='Книга'))
for product in products_q:
    print(product.name)

# Продукты с ценой меньше 20 и в категории 'Одежда'
products_q_exclude = Product.objects.filter(Q(price__lt=20) & ~Q(category__name='Одежда'))
for product in products_q_exclude:
    print(product.name)

# Продукты с названием, содержащим 'Телефон' или с ценой выше 100
products_q_complex = Product.objects.filter(Q(name__icontains='Телефон') | Q(price__gt=100))
for product in products_q_complex:
    print(product.name)
