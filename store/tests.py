from django.urls import reverse
from django.test import TestCase
from .models import Product
from .factories import ProductFactory

class ProductListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем 10 продуктов
        for _ in range(10):
            ProductFactory()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/store/products/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/product_list.html')

    def test_pagination_is_ten(self):
        # Создаем больше продуктов, чем нужно для одной страницы (больше 10)
        ProductFactory.create_batch(15)

        response = self.client.get(reverse('product_list'))

        # Проверяем, что пагинация включена
        self.assertTrue(response.context['is_paginated'])

        # Проверяем, что на странице находится ровно 10 продуктов
        self.assertEqual(len(response.context['products']), 10)

    def test_lists_all_products(self):
        Product.objects.all().delete()  # Удаляем все продукты перед тестом
        ProductFactory.create_batch(10)  # Создаем ровно 10 продуктов
        response = self.client.get(reverse('product_list'))
        self.assertEqual(len(response.context['products']), 10)


class ProductCreateViewTest(TestCase):
    def test_create_product(self):
        product_data = {
            'name': 'New Product',
            'description': 'Test Description',
            'price': '19.99',
            'category': CategoryFactory().id,  # Предполагается, что у вас есть CategoryFactory
            'storage_amount': 10,
        }
        response = self.client.post(reverse('product_create'), data=product_data)
        self.assertEqual(response.status_code, 302)  # Ожидается редирект
        self.assertTrue(Product.objects.filter(name='New Product').exists())


class ProductUpdateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product = ProductFactory(name='Original Product')

    def test_update_product(self):
        response = self.client.post(reverse('product_update', args=[self.product.id]), {
            'name': 'Updated Product',
            'description': 'Updated Description',
            'price': '29.99',
            'category': self.product.category.id,
            'storage_amount': 5,
        })
        self.assertEqual(response.status_code, 302)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated Product')


class ProductDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product = ProductFactory()

    def test_delete_product(self):
        response = self.client.post(reverse('product_delete', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())
