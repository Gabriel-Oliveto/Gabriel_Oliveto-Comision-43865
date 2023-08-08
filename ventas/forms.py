from django import forms
from .models import Auto, Cliente, Venta


class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = "__all__"


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = "__all__"


class BusquedaAutoForm(forms.Form):
    busqueda = forms.CharField(max_length=100, required=False)


class BusquedaClienteForm(forms.Form):
    nombre_cliente = forms.CharField(label="Nombre del cliente", max_length=100)
    apellido_cliente = forms.CharField(label="Apellido del cliente", max_length=100)
