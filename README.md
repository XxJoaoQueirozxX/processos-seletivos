# APP Processos Seletivos
Web APP padrão MVC para acompanhar processos seletivos. Desenvolvido com Python e Flask, nele você pode fazer um CRUD dos seus processos seletivos bem como as etapas desses processos.


##Como rodar o projeto

Para rodar o projeto é preciso criar um ambiente virtual com python e instalar as dependencias para fazer isso você pode seguir a sequência de passos a seguir

### Criando e ativando o ambiente virtual

    python -m venv venv
    venv\Scripts\activate

### Instalando dependências
    
    pip install -r requirements.txt

### Configurando as variaveis e rodando o projeto

##### Windows
    set FLASK_APP=wsgi
    flask run

##### Linux
    export FLASK_APP=wsgi
    flask run
