from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import Clients, Suppliers, Order, Manager, Comment


class ClientForm(ModelForm):
    class Meta:
        model = Clients
        fields = ('adress', 'phone', 'director', 'e_mail')

        widgets = {
            "adress": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'адрес магазина'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'номер телефона'
            }),
            "director": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО директора магазина'

            }),
            "e_mail": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'адрес почты'
            })
        }


class SupplierForm(ModelForm):
    class Meta:
        model = Suppliers
        fields = ('name', 'city')

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название'
            }),
            "city": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'город'
            }),
        }


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('dest', 'supplier', 'name', 'price', 'amount', 'date')
        widgets = {

            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'цена'
            }),
            "amount": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'количество'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'дата и время'
            }),
        }


class ManagerForm(ModelForm):
    class Meta:
        model = Manager
        fields = ('supplier', 'name', 'phone', 'e_mail', 'age')
        widgets = {

            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'имя'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'телефон'
            }),
            "e_mail": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'почта'
            }),
            "age": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'возраст'
            }),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('topic', 'text', 'create_date')
        widgets = {
            "topic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'текст'
            }),
            "create_date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'дата и время'
            }),
        }