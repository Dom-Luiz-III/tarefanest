from django.contrib import admin
from .models import Tarefa

# Filtro para ver os dados que estão armazenados no SQlite
@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao' , 'data', 'status')
    list_filter = ('status',)
    search_fields = ('titulo',)