# blog
# Como começar a contribuir?

### Configurando seu ambiente de desenvolvimento
    

``git clone git@github.com:communitydevpro/blog.git``

``cd blog``

``cp contrib/env-sample .env``

``python -m venv .venv``
 #### linux
    
``source .venv/bin/activate``

#### windows

``.venv\Scripts\Activate ``

#### Instalando dependências

`` pip install -r requirements.txt``

#### aplicando migrações e rodando projeto

``python manage.py makemigrations``

``python manage.py migrate``

``python manage.py runserver``
