from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='category_images', null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='_product_images')
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} {self.description}'


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)

class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина пользователя: {self.user.username}. Товар: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity
