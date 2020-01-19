from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpRequest, HttpResponse
from scraping.models import TechModel
from .forms import TechForms
# Create your views here.

def query_valida(query):
    return query != "" and query is not None

def buscador(request):
    noticias = TechModel.objects.all()
    titulo_query = request.GET.get("title_contains")

    if query_valida(titulo_query):
        noticias = noticias.filter(title__icontains=titulo_query)
    
    return noticias

def index(request):
    noticias = TechModel.objects.all()
    return render(request, "index.html", {"noticias": noticias})

def HomePageView(request):
    noticias = buscador(request)

    return render(request, "index.html", {"noticias": noticias})
    
