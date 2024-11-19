

# Projeto de CRUD de Livros

Este projeto é uma API RESTful para gerenciamento de livros, implementada usando Django e Django Rest Framework.

## Funcionalidades

- Listar todos os livros
- Criar um novo livro
- Visualizar detalhes de um livro específico
- Atualizar informações de um livro
- Deletar um livro
- **Gerenciar coleções de livros associadas a um usuário (colecionador)**
- **Autenticação baseada em Token e permissões para garantir que apenas o colecionador possa gerenciar sua coleção**

## Estrutura do Projeto

O projeto consiste em quatro modelos principais:

1. `Categoria`: Representa as categorias dos livros
2. `Autor`: Representa os autores dos livros
3. `Livro`: Representa os livros, com relações para Categoria e Autor
4. **`Coleção`: Representa uma coleção de livros associada a um usuário**

## Endpoints da API

- `GET /livros/`: Lista todos os livros
- `POST /livros/create`: Cria um novo livro
- `GET /livros/<id>/`: Retorna detalhes de um livro específico
- `PUT /livros/<id>/`: Atualiza um livro específico
- `DELETE /livros/<id>/`: Deleta um livro específico
- **`GET /colecoes/`: Lista todas as coleções do usuário autenticado**
- **`POST /colecoes/create`: Cria uma nova coleção**
- **`GET /colecoes/<id>/`: Retorna detalhes de uma coleção específica**
- **`PUT /colecoes/<id>/`: Atualiza uma coleção específica**
- **`DELETE /colecoes/<id>/`: Deleta uma coleção específica**

## Instalação e Configuração

1. Clone o repositório:
   ```bash
   git clone git@github.com:JOAO2666/biblioteca-django.git
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute as migrações:
   ```bash
   python manage.py migrate
   ```

4. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

## Autenticação e Permissões

Este projeto utiliza autenticação baseada em Token com o Django REST Framework Simple JWT. Para configurar, instale o pacote e adicione as configurações necessárias no `settings.py`.

## Documentação da API

A documentação da API é gerada automaticamente usando o drf-spectacular. Instale o pacote e adicione as configurações e URLs necessárias.

## Testes Automatizados

Para garantir a funcionalidade correta, desenvolvemos testes automatizados. Crie os testes no arquivo `tests.py` e execute-os com:

```bash
python manage.py test
```
