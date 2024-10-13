import os
import django

# Укажите путь к settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_store.settings')
django.setup()

from store.models import  Category, Product

# Создание категорий
#category1 = Category.objects.create(name='Электроника')
#category2 = Category.objects.create(name='Одежда')

# Создание продуктов
#product1 = Product.objects.create(name='Телефон', description='Смарт телефон', price=299.99, category=category1)
#product2 = Product.objects.create(name='Футболка', description='Стильная футболка', price=19.99, category=category2)
#product3 = Product.objects.create(name='Книга', description='Интересная книга', price=9.99, category=category2)

# Все продукты в категории 'Электроника'
category_electronics = Category.objects.get(name='Электроника')
products_in_electronics = category_electronics.products.all()
for product in products_in_electronics:
    print(product.name)

categories = Category.objects.all()

# Примеры запросов

# 1. Получение всех продуктов в определенной категории
def get_products_in_category(category_name):
    try:
        category = Category.objects.get(name=category_name)
        return category.products.all()
    except Category.DoesNotExist:
        return None

# 2. Получение всех заказов (без пользователя)
def get_all_orders():
    return Order.objects.all()

# 3. Получение всех отзывов для конкретного продукта
def get_reviews_for_product(product_name):
    try:
        product = Product.objects.get(name=product_name)
        return product.reviews.all()
    except Product.DoesNotExist:
        return None

# Примеры использования values()
def get_product_details():
    return Product.objects.values('name', 'price')

def get_order_info():
    return Order.objects.values('id', 'is_paid')

def get_product_reviews(product_name):
    try:
        product = Product.objects.get(name=product_name)
        return product.reviews.values('rating', 'comment')
    except Product.DoesNotExist:
        return None

# Примеры использования values_list()
def get_product_names_in_category(category_name):
    try:
        category = Category.objects.get(name=category_name)
        return category.products.values_list('name', flat=True)
    except Category.DoesNotExist:
        return None

def get_order_ids():
    return Order.objects.values_list('id', flat=True)

def get_review_ratings_for_product(product_name):
    try:
        product = Product.objects.get(name=product_name)
        return product.reviews.values_list('rating', flat=True)
    except Product.DoesNotExist:
        return None
