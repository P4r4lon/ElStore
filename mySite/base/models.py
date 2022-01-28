from django.db import models
from django.utils import timezone


class Clients(models.Model):
    adress = models.CharField(max_length=200, verbose_name='Адрес магазина')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    director = models.CharField(max_length=50, verbose_name='Руководитель')
    e_mail = models.CharField(max_length=50, verbose_name='Почта')

    def __str__(self):
        return self.adress

    def get_absolute_url(self):
        return f'/clients/{self.id}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Suppliers(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    city = models.CharField(max_length=50, verbose_name='Город')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/suppliers/{self.id}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

class Order(models.Model):
    dest = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='order', verbose_name='Адрес магазина')
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE, related_name='order_supplier', verbose_name='Поставщик')
    name = models.CharField(max_length=250, verbose_name='Название')
    amount = models.IntegerField(verbose_name='Количество')
    price = models.IntegerField(default=25, verbose_name='Цена')
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/orders_search/{self.id}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Manager(models.Model):
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE, related_name='manager', verbose_name='поставщик')

    name = models.CharField(max_length=50, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    e_mail = models.CharField(max_length=30, verbose_name='Почта')
    age = models.CharField(max_length=3, verbose_name='Возраст')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/managers/{self.id}'

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'


class Comment(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='comment')

    topic = models.CharField(max_length=200, verbose_name='Тема')
    text = models.TextField(verbose_name='Текст')
    create_date = models.DateTimeField(blank=True, null=True, default=timezone.now, verbose_name='Дата')

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return f'/comments/{self.id}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'