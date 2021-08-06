from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Категорія', max_length=150)
    photo = models.ImageField('Фото', upload_to='images/', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class Product(models.Model):
    url = models.SlugField(max_length=130, unique=True)
    product_name = models.CharField('Назва товару', max_length=150)
    description = models.TextField('Опис')
    price = models.PositiveIntegerField('Ціна', default=0, help_text='вказувати суму в гривнях')
    photo = models.ImageField('Фото', upload_to='images/')
    category = models.ForeignKey(Category, verbose_name='Категорія', on_delete=models.PROTECT, null=True)
    availability = models.CharField('Наявність', max_length=150)
    rating_value = models.CharField('Рейтинг', max_length=30, null=True)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField('Значення', default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'Зірка рейтингу'
        verbose_name_plural = 'Зірки рейтингу'
        ordering = ['-value']


class Rating(models.Model):
    ip = models.CharField('IP адреса', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='зірка')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='товар')

    def __str__(self):
        return f'{self.star} - {self.product}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def get_value(self):
        return self.product

