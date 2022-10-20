from django.shortcuts import render
from primerMVT.models import Familiar

# Create your views here.
def index(request):
    return render(request, "/Users/harkonen/Desktop/MVT/mvt_gaston_cordoba/primerMVT/templates/example/saludar.html")

def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "/Users/harkonen/Desktop/MVT/mvt_gaston_cordoba/primerMVT/templates/example/familiares.html", {"lista_familiares": lista_familiares})
