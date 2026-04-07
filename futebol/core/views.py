from django.shortcuts import render, redirect
from .models import Jogador

def lista(request):
    jogadores = Jogador.objects.all()
    return render(request, 'lista.html', {'jogadores': jogadores})

def criar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        time = request.POST.get('time')

        Jogador.objects.create(nome=nome, idade=idade, time=time)
        return redirect('/')

    return render(request, 'criar.html')

def editar(request, id):
    jogador = Jogador.objects.get(id=id)

    if request.method == 'POST':
        jogador.nome = request.POST.get('nome')
        jogador.idade = request.POST.get('idade')
        jogador.time = request.POST.get('time')
        jogador.save()
        return redirect('/')

    return render(request, 'editar.html', {'jogador': jogador})

def deletar(request, id):
    jogador = Jogador.objects.get(id=id)
    jogador.delete()
    return redirect('/')