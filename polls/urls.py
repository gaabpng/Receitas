from django.urls import path
from .views import index, lista_receitas, detalhes_receita, adicionar_receita, buscar_receitas, cadastro

app_name = 'polls'

urlpatterns = [
    path('', index, name='index'),
    path('lista/', lista_receitas, name='lista_receitas'),
    path('detalhes/<int:receita_id>/', detalhes_receita, name='detalhes_receita'),
    path('adicionar/', adicionar_receita, name='adicionar_receita'),
    path('buscar/', buscar_receitas, name="buscar_receitas"),
    path('cadastro/', cadastro, name="cadastro"),
]