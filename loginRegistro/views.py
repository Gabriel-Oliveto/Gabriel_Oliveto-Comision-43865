from django.shortcuts import render
from .models import Avatar
from .forms import (
    RegistroUsuariosForm,
    UsuarioEditForm,
    AvatarFormulario,
)
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):
    return render(request, "ventas/index.html")


# ------------Login, logout, Registracion, Avatar------------#


def loguin_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar
                return render(
                    request,
                    "loginRegistro/index.html",
                    {"mensaje": f"Bienvenido/a {usuario}"},
                )
            else:
                return render(
                    request,
                    "loginRegistro/login.html",
                    {"form": form, "mensaje": "Datos Invalidos"},
                )
        else:
            return render(
                request,
                "loginRegistro/login.html",
                {"form": form, "mensaje": "Datos Invalidos"},
            )

    form = AuthenticationForm()
    return render(request, "loginRegistro/login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = RegistroUsuariosForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            form.save()
            return render(
                request, "loginRegistro/index.html", {"mensaje": "Usuario Creado"}
            )
    else:
        form = RegistroUsuariosForm()

    return render(request, "loginRegistro/registro.html", {"form": form})


class EditarPerfilView(LoginRequiredMixin, ListView):
    def post(self, request):
        usuario = request.user
        form = UsuarioEditForm(request.POST)
        if form.is_valid():
            usuario.nombre = form.cleaned_data.get("nombre")
            usuario.apellido = form.cleaned_data.get("apellido")
            usuario.email = form.cleaned_data.get("email")
            usuario.password1 = form.cleaned_data.get("password1")
            usuario.password2 = form.cleaned_data.get("password2")
            usuario.save()
            return render(
                request,
                "loginRegistro/index.html",
                {
                    "mensaje": f"Se actualizaron los datos del usuario {usuario.username} correctamente"
                },
            )
        else:
            return render(request, "loginRegistro/editarPerfil.html", {"form": form})

    def get(self, request):
        usuario = request.user
        form = UsuarioEditForm(instance=usuario)
        return render(
            request,
            "loginRegistro/editarPerfil.html",
            {"form": form, "usuario": usuario.username},
        )


class AgregarAvatarView(LoginRequiredMixin, ListView):
    def get(self, request):
        form = AvatarFormulario()
        return render(request, "loginRegistro/agregarAvatar.html", {"form": form})

    def post(self, request):
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = request.user
            avatarAnterior = Avatar.objects.filter(user=u)
            if len(avatarAnterior) > 0:
                avatarAnterior[0].delete()
            avatar = Avatar(user=u, imagen=form.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "loginRegistro/index.html")
        return render(request, "loginRegistro/agregarAvatar.html", {"form": form})
