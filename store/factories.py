import factory
from factory.django import DjangoModelFactory
from .models import Product, Category

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    description = factory.Faker('text')
    price = factory.Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
    image = factory.django.ImageField(color='blue')
    category = factory.SubFactory(CategoryFactory)
    storage_amount = factory.Faker('random_int', min=0, max=100)
