# Bem Vindo

Este repositório irá desenvolver uma aplicação web de cadastro de receitas utilizando a linguagem Python e o framework Django para o back-end e a framework AngularJs para o front-ent.

O objetivo é mostrar, através da wiki um tutorial mostrando as funcionalidades das frameworks e o quanto elas agilizam o desenvolvimento de aplicações web.

Todos os exemplos serão feitos utilizando o terminal do linux e o editor de texto Sublime Text.

## Pré Requisitos:
	
	* Python3
	* python3-dev
	* libpq-dev
	* Virtualenv	
	* Postgres >= 9.3
	* Angular <= 1.5
	* Bootstrap <= 3.3.7
	* Jquery <= 3.1.1

## Instalação

### Configuração do ambiente

Faça o download do projeto no link ou se possuir o git instalado execute o comando abaixo na pasta em que deseja salvar o projeto.

	git clone https://github.com/asleao/receitas-da-familia.git

Em seguida vá até a pasta onde o projeto foi salvo e crie o ambiente virtual python com o seguinte comando:
	
	virtualenv -p python3 env

Ative-o:

	source env/bin/activate

Instale as dependências:

	pip install -r requirements.txt

Nota: Caso receba um erro com framework psycopg2, lembre-se de que as dependências python3-dev e libpq-dev devem estar instaladas antes do procedimento acima ser executado. No Ubuntu, para instalá-las basta executar o comando:
	
	sudo apt-get install python3-dev libpq-dev

### Banco de dados:

Crie um banco de dados com o nome "receitas" em seu postgres. Caso queira outro nome, vá até o arquivo "settings.py", seção "Databases", na pasta project e altere seu nome.

Para criar as tabelas no banco, execute o comando:

	python3 manage.py migrate

### Administração

Para criar um usuário adminstrador execute o comando:

	python3 manage.py createsuperuser

### Execução

Para executar o projeto, em um terminal, execute o seguinte comando:

	python3 manage.py runserver




