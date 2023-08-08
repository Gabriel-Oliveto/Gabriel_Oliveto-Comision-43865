from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Auto, Cliente, Venta
from .forms import (
    AutoForm,
    ClienteForm,
    BusquedaAutoForm,
    VentaForm,
    BusquedaClienteForm,
)
from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):
    return render(request, "ventas/index.html")


# ------------Class Views Auto------------#


# Vista protegida con LoginRequiredMixin
class AgregarAutoView(LoginRequiredMixin, ListView):
    def get(self, request):
        form = AutoForm()
        return render(request, "ventas/agregar_auto.html", {"form": form})

    def post(self, request):
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("buscar_auto")
        return render(request, "ventas/agregar_auto.html", {"form": form})


# Vistas protegidas con LoginRequiredMixin
class BuscarAutoView(LoginRequiredMixin, ListView):
    def get(self, request):
        form = BusquedaAutoForm()
        resultados = Auto.objects.all()
        return render(
            request,
            "ventas/buscar_auto.html",
            {"form": form, "resultados": resultados},
        )

    def post(self, request):
        form = BusquedaAutoForm(request.POST)
        if form.is_valid():
            busqueda = form.cleaned_data["busqueda"]
            resultados = Auto.objects.filter(marca__icontains=busqueda)
            form = BusquedaAutoForm()
        else:
            resultados = Auto.objects.all()
        return render(
            request,
            "ventas/buscar_auto.html",
            {"form": form, "resultados": resultados},
        )


# Vista protegida con LoginRequiredMixin
class ActualizarAutoView(LoginRequiredMixin, ListView):
    def get(self, request, id_auto):
        auto = Auto.objects.get(id=id_auto)
        form = AutoForm(
            initial={
                "marca": auto.marca,
                "modelo": auto.modelo,
                "precio": auto.precio,
            }
        )
        return render(request, "ventas/actualizar_auto.html", {"form": form})

    def post(self, request, id_auto):
        auto = Auto.objects.get(id=id_auto)
        form = AutoForm(request.POST)
        if form.is_valid():
            auto.marca = form.cleaned_data.get("marca")
            auto.modelo = form.cleaned_data.get("modelo")
            auto.precio = form.cleaned_data.get("precio")
            auto.save()
            return redirect(reverse_lazy("buscar_auto"))
        return render(request, "ventas/updateAuto.html", {"form": form})


# Vista protegida con LoginRequiredMixin
class BorrarAutoView(LoginRequiredMixin, DeleteView):
    model = Auto
    success_url = reverse_lazy("buscar_auto")
    template_name = "ventas/borrar_auto.html"


# ------------Class Views Cliente------------#


# En la vista agregar_cliente
class AgregarClienteView(LoginRequiredMixin, ListView):
    def get(self, request):
        ctx = {"clientes": Cliente.objects.all()}
        form = ClienteForm()
        return render(request, "ventas/agregar_cliente.html", {"form": form})

    def post(self, request):
        ctx = {"clientes": Cliente.objects.all()}
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "ventas/buscar_cliente.html", ctx)
        return render(request, "ventas/agregar_cliente.html", {"form": form})


# Vista protegida con LoginRequiredMixin
class BuscarClienteView(LoginRequiredMixin, ListView):
    def get(self, request):
        ctx = {"clientes": Cliente.objects.all()}
        return render(request, "ventas/buscar_cliente.html", ctx)

    def post(self, request):
        query = request.POST.get("query")
        clientes = Cliente.objects.filter(
            Q(nombre__icontains=query)
            | Q(apellido__icontains=query)
            | Q(direccion__icontains=query)
        )
        return render(
            request,
            "ventas/buscar_cliente.html",
            {
                "clientes": clientes,
            },
        )


# Vista protegida con LoginRequiredMixin
class ActualizarClienteView(LoginRequiredMixin, ListView):
    def get(self, request, id_cliente):
        cliente = Cliente.objects.get(id=id_cliente)
        form = ClienteForm(
            initial={
                "nombre": cliente.nombre,
                "apellido": cliente.apellido,
                "direccion": cliente.direccion,
            }
        )
        return render(request, "ventas/actualizar_cliente.html", {"form": form})

    def post(self, request, id_cliente):
        cliente = Cliente.objects.get(id=id_cliente)
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente.nombre = form.cleaned_data.get("nombre")
            cliente.apellido = form.cleaned_data.get("apellido")
            cliente.direccion = form.cleaned_data.get("direccion")
            cliente.save()
            return redirect(reverse_lazy("buscar_cliente"))
        return render(request, "ventas/updateCliente.html", {"form": form})


# Vista protegida con LoginRequiredMixin
class BorrarClienteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy("buscar_cliente")
    template_name = "ventas/borrar_cliente.html"


# ------------Class Views Venta------------#


# Vista protegida con LoginRequiredMixin
class RealizarVentaView(LoginRequiredMixin, ListView):
    def get(self, request):
        form = VentaForm()
        return render(request, "ventas/realizar_venta.html", {"form": form})

    def post(self, request):
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("buscar_ventas")
        return render(request, "ventas/realizar_venta.html", {"form": form})


# Vista protegida con LoginRequiredMixin
class BuscarVentaView(LoginRequiredMixin, ListView):
    def get(self, request):
        form = BusquedaClienteForm()
        ventas = Venta.objects.all()
        return render(
            request, "ventas/buscar_ventas.html", {"form": form, "ventas": ventas}
        )

    def post(self, request):
        form = BusquedaClienteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre_cliente"]
            apellido = form.cleaned_data["apellido_cliente"]
            cliente = Cliente.objects.filter(
                nombre__icontains=nombre, apellido__icontains=apellido
            ).first()
            if cliente:
                ventas = Venta.objects.filter(cliente=cliente)
            else:
                ventas = Venta.objects.all()
        else:
            ventas = Venta.objects.all()

        return render(
            request, "ventas/buscar_ventas.html", {"form": form, "ventas": ventas}
        )


# Vista protegida con LoginRequiredMixin
class ActualizarVentaView(LoginRequiredMixin, ListView):
    def get(self, request, id_venta):
        venta = Venta.objects.get(id=id_venta)
        form = VentaForm(
            initial={
                "auto": venta.auto,
                "cliente": venta.cliente,
                "fecha": venta.fecha,
            }
        )
        return render(request, "ventas/actualizar_venta.html", {"form": form})

    def post(self, request, id_venta):
        venta = Venta.objects.get(id=id_venta)
        form = VentaForm(request.POST)
        if form.is_valid():
            venta.auto = form.cleaned_data.get("auto")
            venta.cliente = form.cleaned_data.get("cliente")
            venta.fecha = form.cleaned_data.get("fecha")
            venta.save()
            return redirect(reverse_lazy("buscar_ventas"))
        return render(request, "ventas/actualizar_venta.html", {"form": form})


# Vista protegida con LoginRequiredMixin
class BorrarVentaView(LoginRequiredMixin, DeleteView):
    model = Venta
    success_url = reverse_lazy("buscar_ventas")
    template_name = "ventas/borrar_venta.html"


# ACERCA DE MI
def about(request):
    return render(request, "ventas/acercaDeMi.html", {})
