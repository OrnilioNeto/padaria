from django.shortcuts import render
#está importando a classe HttpResponse do pacote django.shortcuts do framework Django.
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
#from .models import Agendamento
#from .forms import AgendamentoForm
from django.shortcuts import render
#from .models import Agendamento

# Create your views here.


# def home(request):
#     return render(request,'home/index.html')

def home2(request):
    return render(request,'home2.html')
    
# def home3(request):
#     return render(request,'home2/home3.html')