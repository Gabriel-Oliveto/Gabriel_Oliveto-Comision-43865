from django.contrib import admin
from .models import Auto, Cliente, Venta

# Register your models here.
admin.site.register(Auto)
admin.site.register(Cliente)
admin.site.register(Venta)
