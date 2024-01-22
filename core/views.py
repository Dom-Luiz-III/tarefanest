from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views import View
from .models import Tarefa

from .forms import TarefaForm
from .models import Tarefa

# Método que chama o index.html + outros dados como os atributos da classe tarefa
def index(request):
    tarefas = Tarefa.objects.all()

    context = {
        'tarefas': tarefas,
    }
    return render(request, 'index.html', context)


# Método feito para criar uma tarefa nova pela página HTML
def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TarefaForm()

    return render(request, 'index.html', {'form': form})

# Método feito para alterar o status da tarefa pela página HTML
@require_POST
def alterar_status(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    novo_status = request.POST.get('novo_status')

    if novo_status in ['pendente', 'executando', 'concluida']:
        tarefa.status = novo_status
        tarefa.save()

    return redirect('index')

class ApagarTarefaView(View):
    def post(self, request, tarefa_id):
        tarefa = get_object_or_404(Tarefa, id=tarefa_id)
        tarefa.delete()
        return redirect('index')