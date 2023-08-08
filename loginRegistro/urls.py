from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.index, name="inicio"),
    # paths loguin
    path("login/", views.loguin_request, name="login"),
    path("logout/", LogoutView.as_view(template_name="loginRegistro/logout.html"),name="logout",),
    path("register/", views.register, name="register"),
    path("editarlPerfil/", views.EditarPerfilView.as_view(), name="editarlPerfil"),
    path("agregarAvatar/", views.AgregarAvatarView.as_view(), name="agregarAvatar"),
]