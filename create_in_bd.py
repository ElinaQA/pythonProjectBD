import os
import django

# Укажите путь к settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_store.settings')
django.setup()

from store.models import Product

# Создание продуктов
#product1 = Product.objects.create(name='Телефон', description='Смарт телефон', price=299.99)
#product2 = Product.objects.create(name='Футболка', description='Стильная футболка', price=19.99)
#product3 = Product.objects.create(name='Книга', description='Интересная книга', price=9.99)

# Запрашиваем все записи
products = Product.objects.all()
for product in products:
    print(product.name, product.description, product.price)

