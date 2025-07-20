from django.shortcuts import render, redirect
from .models import Agendamento

def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'core/lista_agendamentos.html', {'agendamentos':agendamentos})

def cadastro_agendamentos(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        data_e_hora = request.POST.get('data_e_hora')
        telefone = request.POST.get('telefone')
        diagnostico = request.POST.get('diagnostico')

        Agendamento.objects.create(
            nome=nome,
            data_e_hora_agendamento=data_e_hora,
            telefone=telefone,
            diagnostico=diagnostico
        )

        return redirect('lista_agendamentos')
    
    return render(request, 'core/cadastro_agendamentos.html')

def total_agendamentos(request):
    total_agendamentos = Agendamento.objects.count()
    return render(request, 'core/home.html', {'total_agendamentos': total_agendamentos})
