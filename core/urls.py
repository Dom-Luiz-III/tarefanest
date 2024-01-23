from django.urls import path
from .views import index, criar_tarefa, alterar_status, ApagarTarefaView, criar_tarefa_pagina, tarefa_disponivel

#URLs da página
urlpatterns = [
    path('', index, name='index'),
    path('inicio', index, name='inicio'), 
    path('criar_tarefa_pagina', criar_tarefa_pagina, name='criar_tarefa_pagina'),
    path('tarefa_disponivel', tarefa_disponivel, name='tarefa_disponivel'),
    path('criar_tarefa/', criar_tarefa, name='criar_tarefa'),
    path('alterar_status/<int:tarefa_id>/', alterar_status, name='alterar_status'),  
    path('apagar_tarefa/<int:tarefa_id>/', ApagarTarefaView.as_view(), name='apagar_tarefa'),
]
