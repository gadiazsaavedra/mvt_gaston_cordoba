from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "/Users/harkonen/Desktop/MVT/mvt_gaston_cordoba/primerMVT/templates/example/saludar.html")