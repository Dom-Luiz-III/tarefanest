from django.urls import path
from .views import index, criar_tarefa, alterar_status

#URLs da página
urlpatterns = [
    path('', index, name='admin'),
    path('', index, name='index'),
    path('home/', index, name='home'),  
    path('criar_tarefa/', criar_tarefa, name='criar_tarefa'),
    path('alterar_status/<int:tarefa_id>/', alterar_status, name='alterar_status'),  
]
