# Teste - Brain Agriculture

O teste tem como objetivo acurar as habilidades do candidato em resolver alguns problemas relacionados à lógica de programação, regra de negócio e orientação à objetos.

O mesmo consiste em um cadastro de produtor rural com os seguintes dados:

1.  CPF ou CNPJ
2.  Nome do produtor
3.  Nome da Fazenda
4.  Cidade
5.  Estado
6.  Área total em hectares da fazenda
7.  Área agricultável em hectares
8.  Área de vegetação em hectares
9.  Culturas plantadas (Soja, Milho, Algodão, Café, Cana de Açucar)

# Requisitos de negócio

- O usuário deverá ter a possibilidade de cadastrar, editar, e excluir produtores rurais.
- O sistema deverá validar CPF e CNPJ digitados incorretamente.
- A soma de área agrícultável e vegetação, não deverá ser maior que a área total da fazenda
- Cada produtor pode plantar mais de uma cultura em sua Fazenda.
- A plataforma deverá ter um Dashboard que exiba:
  - Total de fazendas em quantidade
  - Total de fazendas em hectares (área total)
  - Gráfico de pizza por estado.
  - Gráfico de pizza por cultura.
  - Gráfico de pizza por uso de solo (Área agricultável e vegetação)

# Requisitos técnicos

- O desenvolvedor front-end deverá utilizar:

  - [ReactJS](http://reactjs.org);
  - [Redux](https://redux.js.org/) para controlar o estado da aplicação.
    - Caso entenda que faça sentido, utilize [Context API](https://reactjs.org/docs/context.html) como recurso adicional ou substituto ao Redux (Opcional)
  - Crie pelo menos um teste unitário por componente (Opcional)
  - A criação das estruturas de dados "mockados" faz parte da avaliação.

- O desenvolvedor back-end deve:
  - Salvar os dados em um banco de dados Postgres usando o NodeJS como layer de Backend, e entregar os endpoints para cadastrar, editar, e excluir produtores rurais, além do endpoint que retorne os totais para o dashboard.
  - A criação das estruturas de dados "mockados" faz parte da avaliação.

  Desejável:
  - TypeScript
  - Conceitos como SOLID, KISS, Clean Code, API Contracts, Tests, Layered Architecture

  Bonus:
  - Aplicação disponibilizada em algum cloud provider de sua preferência

- O desenvolvedor full-stack deve realizar ambos, e concluir a integração.
  > Não envie a solução como anexo, suba os fontes para seu Github (ou outro repositório) e envie o link para o avaliador.


---

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



