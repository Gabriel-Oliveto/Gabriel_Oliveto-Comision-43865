from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="inicio"),
    # paths Auto
    path("agregar_auto/", views.AgregarAutoView.as_view(), name="agregar_auto"),
    path("buscar_auto/", views.BuscarAutoView.as_view(), name="buscar_auto"),
    path("actualizar_auto/<id_auto>/", views.ActualizarAutoView.as_view(), name="actualizar_auto"),
    path("borrar_auto/<int:pk>/", views.BorrarAutoView.as_view(), name="borrar_auto"),
    # paths Cliente
    path("agregar_cliente/", views.AgregarClienteView.as_view(), name="agregar_cliente"),
    path("buscar_cliente/", views.BuscarClienteView.as_view(), name="buscar_cliente"),
    path("actualizar_cliente/<id_cliente>/", views.ActualizarClienteView.as_view(), name="actualizar_cliente"),
    path("borrar_cliente/<int:pk>/", views.BorrarClienteView.as_view(), name="borrar_cliente"),
    # paths Venta
    path("realizar_venta/", views.RealizarVentaView.as_view(), name="realizar_venta"),
    path("buscar_ventas/", views.BuscarVentaView.as_view(), name="buscar_ventas"),
    path("actualizar_venta/<id_venta>/", views.ActualizarVentaView.as_view(), name="actualizar_venta"),
    path("borrar_venta/<int:pk>/", views.BorrarVentaView.as_view(), name="borrar_venta"),
    # path Acerca de Mi
    path("acercaDeMi/", views.about, name="acercaDeMi"),
]