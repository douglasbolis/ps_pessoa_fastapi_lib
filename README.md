# ps_pessoa_fastapi_lib

[![Test, Deploy Lib and FastAPI Service](https://github.com/douglasbolis/ps_pessoa_fastapi_lib/actions/workflows/test-and-deploy-lib.yml/badge.svg)](https://github.com/douglasbolis/ps_pessoa_fastapi_lib/actions/workflows/test-and-deploy-lib.yml)

Lib de Cadastro de Pessoas e Endereços desenvolvida com SQLModel.
Aplicação de Cadastro de Pessoas e Endereços desenvolvida com FastAPI e a lib implementada.

## Visão Geral

Aplicação com MVC e FastAPI + SQLModel.
Este projeto simula o funcionamento de um banco de pessoas, permitindo o cadastro e gerenciamento de pessoas e endereços. Utiliza FastAPI para a API REST e SQLModel para o mapeamento dos modelos e persistência em banco de dados.

A lib contém a parte do Model, com as definições do modelo de Pessoa e Endereço, além da comunicação com o banco de dados(SQLModel).
A aplicação contém os controllers e views configurados usando o FastAPI + a lib instalada via pip.

## Funcionalidades

- Cadastro de pessoas
- Cadastro de endereços
- Validações automáticas via FastAPI

## Requisitos

- [Python 3.11+](https://www.python.org/about/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/)

## Ambiente do projeto

### Baixando o código

```bash
git clone https://github.com/douglasbolis/ps_pessoa_fastapi_lib.git
cd ps_pessoa_fastapi_lib
```

### Ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### Instalação dos pacotes

```bash
pip install -r requirements.txt
```

Pode ser que dê problema, então instale os pacotes separadamente.

```bash
pip install sqlmodel "fastapi[standard]" ps_pessoas_fastapi_lib
```

## Publicação da LIB
---

## Execução

```bash
fastapi dev app/main.py # Linux/Mac
fastapi dev .\app\main.py # Windows
```

Acesse a documentação interativa em [http://localhost:8000/docs](http://localhost:8000/docs).

## Estrutura do Projeto

```bash
.
├── LICENSE                     # Licença do projeto
├── README.md                   # Documentação do projeto
├── app
│   ├── controller              # Rotas e lógica de negócio
│   │   ├── __initi__.py
│   │   ├── endereco.py
│   │   ├── generic.py
│   │   └── pessoa.py
│   └── main.py                 # Inicialização da aplicação FastAPI
├── app.db                      # Banco de dados em memória
├── ps_pessoas_fastapi_lib      # Minha Biblioteca LIB (Model, Repository, Service)
│   ├── __init__.py             # Marca 'ps_pessoas_fastapi_lib' como o módulo principal
│   ├── model                   # Modelos e DTOs
│   │   ├── __init__.py
│   │   ├── dto.py
│   │   └── models.py
│   ├── repository              # Repositórios de acesso a dados
│   │   ├── __init__.py
│   │   └── base.py
│   ├── service                 # Serviços de negócio
│   │   ├── __init__.py
│   │   └── base.py
│   └── util                    # Utilitários e configuração do banco
│       ├── __init__.py
│       └── database.py
├── requirements.txt            # Pacotes (dependências) para instalação
└── setup.py                    # Configuração para a publicação da lib no 'pip')
```

## Licença

Este projeto está sob a licença MIT.
