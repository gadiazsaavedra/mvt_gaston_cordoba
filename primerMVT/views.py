from django.shortcuts import render
from primerMVT.models import Familiar
from django.http import HttpResponse

# Create your views here.


def index(request) -> HttpResponse:

    return render(
        request,
        "example/saludar.html",
    )


def mostrar_familiares(request) -> HttpResponse:
    lista_familiares = Familiar.objects.all()
    return render(
        request,
        "example/familiares.html",
        {"lista_familiares": lista_familiares},
    )
