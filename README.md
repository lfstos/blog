# blog
# Como começar a contribuir?

#### Materiais de apoio:

https://opensource.guide/pt/how-to-contribute/#como-submeter-uma-contribui%C3%A7%C3%A3o

https://docs.github.com/pt/get-started/quickstart/contributing-to-projects

### Configurando seu ambiente de desenvolvimento
    

``git clone git@github.com:communitydevpro/blog.git``

``cd blog``

`` git checkout -b nome_da_nova_branch ``

``python -m venv .venv``

 #### linux
 
 ``cp contrib/env-sample .env``
    
``source .venv/bin/activate``

#### windows

`` você deve copiar o arquivo env-sample e colar na raiz do projeto com o nome de .env ``

``.venv\Scripts\Activate ``

#### Instalando dependências

`` pip install -r requirements.txt``

#### aplicando migrações e rodando projeto

``python manage.py makemigrations``

``python manage.py migrate``

``python manage.py runserver``
