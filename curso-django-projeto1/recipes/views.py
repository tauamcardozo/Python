#from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#def sobre(request):
#    return render(request, 'recipes/sobre.html')

def home(request):
    return render(request, 'recipes/pages/home.html')

#def contato(request):
#    return render(request,'recipes/contato.html', context={
#        'nome': 'Tauam Cardozo',
#        'idade': 30,
#        'email': 'tauamcardozo@gmail.com',
#        'telefone': '22992380191',
#        'profissao': 'Programador',
#        'linguagem': 'Python',
#        'habilidades': ['Django', 'ADVPL'],
#    })
