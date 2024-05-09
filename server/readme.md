# Rural Producers API

---

## Visão Geral

Rural Producers API é uma API RESTful baseada em Python, construída com Django e Django Ninja. Ela serve como uma plataforma para gerenciar dados de produtores rurais, fornecendo endpoints para operações CRUD nas informações dos produtores. A API segue uma arquitetura em três camadas, consistindo de modelos, serviços e controladores, para garantir modularidade, manutenibilidade e escalabilidade.

## Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

- Python 3.12.3: Utilizado como linguagem principal de programação.
- Django: Framework web em Python.
- Django Ninja: Framework para construção de APIS com django 
- PostgreSQL: Banco de dados.
- Docker: Utilizado para a criação de containers e facilitar o ambiente de desenvolvimento e implantação.
- [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer): Gerenciador de depêndencias 


## Execução do projeto

Siga estes passos para inicializar a aplicação usando Docker Compose:

1. Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.
2. Clone o repositório do projeto para o seu ambiente local.
3. Navegue até o diretório raiz do projeto.
4. Crie um arquivo `.env` no diretório raiz do projeto e configure as variáveis de ambiente necessárias.
5. Execute o seguinte comando para construir e iniciar os contêineres:

```bash
docker-compose up --build
```

6. Aguarde até que todos os contêineres sejam construídos e a aplicação esteja pronta para uso.
7. Acesse a aplicação em seu [navegador](http://localhost:8000) ou cliente de API.


### Execução manual

1. Instale o [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)
2. Execute `poetry shell`
3. Instale as depêndencias com `poetry install`
3. Configure a `.env` na pasta **CONFIG**
4. Rode o projeto com `python manage.py runserver` 

---

## Documentação 

Para acessar a documentação da API acesse [localhost](http://localhost:8000/docs)

## Testes 

1. Execute `poetry run pytest --cov ./api` para rodar todos os testes ou `poetry run pytest ./api/tests/<caminho_do_test>` para executar um(a) módulo/teste em especifíco. Caso deseje visualizar a cobertura de testes basta adicionar `--cov`.

## Linter
1. Estamos utilizando `black` como linter, para executa-lo basta executar o comando `poetry run black ./api`



