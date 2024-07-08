# Cadastro
## Formulário para envio de curriculos usando Django.


## Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
- [Git](https://git-scm.com)
- [Python](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)

## Instalação

Siga estas etapas para configurar o ambiente de desenvolvimento:

1. Clone o repositório
```bash
git clone https://github.com/theussilvas/Cadastro.git
cd Myapp

2. Crie e ative um ambiente virtual
```bash
python -m venv venv
# No Windows
venv\Scripts\activate
# No Unix ou MacOS
source venv/bin/activate
```
3. Instale as dependências usando o arquivo `requirements.txt`
```bash
pip install -r requirements.txt
```
4. Configure o banco de dados
   ```bash
   python manage.py migrate


## Para testar o envio de email use o site:
  https://ethereal.email/create
  ## Com ele é possível criar um servidor temporário para recebimentos de emails.
  
  ## Altere as esse campos no settings.py
     EMAIL_HOST_USER = ''  #username/email
     EMAIL_FROM_USER = '' #username/email
     EMAIL_HOST_PASSWORD = '' #password
     Troque pelas informações ao dar create no site.

