from django.db import models



class Candidato(models.Model): 
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cargo = models.CharField(max_length=255)
    ESCOLARIDADE_CHOICES = [
        ('fundamental_incompleto', 'Fundamental Incompleto'),
        ('fundamental_completo', 'Fundamental Completo'),
        ('medio_incompleto', 'Médio Incompleto'),
        ('medio_completo', 'Médio Completo'),
        ('superior_incompleto', 'Superior Incompleto'),
        ('superior_completo', 'Superior Completo'),
    ]
    escolaridade = models.CharField(max_length=50, choices=ESCOLARIDADE_CHOICES)
    observacoes = models.TextField(blank=True, null=True)
    data_envio = models.DateTimeField()
    endereco_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, blank=True, null=True)
    arquivo = models.FileField(upload_to='arquivos_candidatos/')