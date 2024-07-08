from django.urls import path,include
from . import views
from .views import CadastroView,sucess_view


urlpatterns =[
    path('',views.index, name ='index'),
    path('inscricao',CadastroView.as_view(), name ='cadastro'),
    path('success/', sucess_view, name='success_view'),

]