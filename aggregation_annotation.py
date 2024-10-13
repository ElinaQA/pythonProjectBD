import os
import django

# Укажите путь к settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_store.settings')
django.setup()

from store.models import Category, Product
from django.db.models import Avg, Max, Min

# Средняя цена продуктов
avg_price = Product.objects.aggregate(Avg('price'))
print(f"Средняя цена: {avg_price['price__avg']}")

# Максимальная цена продуктов
max_price = Product.objects.aggregate(Max('price'))
print(f"Максимальная цена: {max_price['price__max']}")

# Минимальная цена продуктов
min_price = Product.objects.aggregate(Min('price'))
print(f"Минимальная цена: {min_price['price__min']}")
