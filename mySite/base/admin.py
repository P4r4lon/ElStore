from django.contrib import admin
from .models import Clients, Suppliers, Order, Manager, Comment

admin.site.register(Clients)
admin.site.register(Suppliers)
admin.site.register(Order)
admin.site.register(Manager)
admin.site.register(Comment)