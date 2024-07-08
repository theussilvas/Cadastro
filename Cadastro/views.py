from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import CandidatoForm
from datetime import datetime
from django.views.generic.edit import FormView
from django.conf import settings
from django.core.mail import EmailMessage






def index(request):
    return render(request, 'Cadastro/index.html')


class CadastroView(FormView):
    template_name = 'Cadastro/inscricao.html'
    form_class = CandidatoForm
    success_url = reverse_lazy('success_view')


    def form_valid(self, form):  
        candidato = form.save(commit=False)
        candidato.endereco_ip = self.obterIp(self.request)
        candidato.data_envio = datetime.now()

        candidato.save()
        send = self.EnviarEmail(form)
        return super().form_valid(form)
    

    def obterIp(self,request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0] 
        else:
            ip = request.META.get('REMOTE_ADDR')  
        return ip


    def EnviarEmail(self,form):
        
        campos = form.cleaned_data

        nome = campos['nome']
        email = campos['email']
        tel = campos['telefone']
        cargo = campos['cargo']
        escol = campos['escolaridade']
        obs = campos['observacoes']
        data = datetime.now
        ip = self.obterIp(self.request)

        mensagem = f'Olá {nome},\n\n' \
           f'Seu e-mail é {email} e seu telefone é {tel}.\n' \
           f'Você se candidatou para o cargo de {cargo} com escolaridade {escol}.\n' \
           f'Observações: {obs}\n' \
           f'Data de envio: {data}\n' \
           f'Seu IP: {ip}'


        email = EmailMessage(subject=nome,body=mensagem,from_email=settings.EMAIL_FROM_USER,to=[email])
        email.send()
        return

        
       


def sucess_view(request):
    return render(request,'Cadastro/sucess.html')    
    




    