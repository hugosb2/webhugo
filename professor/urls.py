from django.urls import path
from . import views
urlpatterns = [
    path("cadastrarprofessor/", views.cadastrar, name="cadastrar_professor"),
    path("listarprofessor/", views.listar, name="listar_professor"),
]