from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Imovel
# Create your views here.

imoveis = Imovel.objects.all() #retorna lista

@login_required(login_url="/auth/login")
def home(request):
    return render(request, 'home.html', {'imoveis': imoveis})