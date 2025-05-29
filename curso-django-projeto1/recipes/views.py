from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def sobre(request):
    return HttpResponse('Nome:Tauam Cardozo!')

def home(request):
    return render(request, 'recipes/home.html')

def contato(request):
    return HttpResponse('Telefone:22992380191')
