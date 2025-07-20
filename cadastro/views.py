from django.shortcuts import render

def homepage(request):
    nome = 'Bruno'
    pessoa = {
        'nome':'Maria',
        'idade': 30,
        'cidade':'São Paulo'
    }
    return render(request, 'home.html', {'nome':nome, 'pessoa':pessoa})

def about(request):
    frutas = ['Maçã', 'Uva', 'Banana', 'Mamão']
    return render(request, 'about.html', {'frutas':frutas})