

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

O projeto consiste em três modelos principais:

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
   git clone git@github.com:JOAO2666/solu-o-da-atividade.git
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

Este projeto utiliza autenticação baseada em Token com o Django REST Framework Simple JWT. Para configurar:

1. Instale as dependências:
   ```bash
   pip install djangorestframework-simplejwt
   ```

2. Adicione as configurações no `settings.py`:
   ```python
   INSTALLED_APPS = [
       ...
       'rest_framework',
       'rest_framework_simplejwt.token_blacklist',
   ]

   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': (
           'rest_framework_simplejwt.authentication.JWTAuthentication',
       ),
   }

   SIMPLE_JWT = {
       'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
       'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
       ...
   }
   ```

## Documentação da API

A documentação da API é gerada automaticamente usando o drf-spectacular.

1. Instale o drf-spectacular:
   ```bash
   pip install drf-spectacular
   ```

2. Adicione as configurações no `settings.py`:
   ```python
   INSTALLED_APPS = [
       ...
       'drf_spectacular',
   ]

   REST_FRAMEWORK = {
       ...
       'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
   }

   SPECTACULAR_SETTINGS = {
       'TITLE': 'Book Collection API',
       'DESCRIPTION': 'API for managing book collections',
       'VERSION': '1.0.0',
   }
   ```

3. Adicione as URLs para a documentação:
   ```python
   from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

   urlpatterns = [
       ...
       path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
       path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
   ]
   ```

## Testes Automatizados

Para garantir a funcionalidade correta, desenvolvemos testes automatizados:

1. Crie os testes no arquivo `tests.py`:
   ```python
   from django.test import TestCase
   from django.contrib.auth.models import User
   from .models import Book, Collection

   class CollectionTestCase(TestCase):
       def setUp(self):
           self.user = User.objects.create_user(username='testuser', password='12345')
           self.book = Book.objects.create(title='Test Book', author='Author', published_date='2023-01-01')
           self.collection = Collection.objects.create(user=self.user, name='Test Collection')
           self.collection.books.add(self.book)

       def test_collection_creation(self):
           self.assertEqual(self.collection.name, 'Test Collection')
           self.assertIn(self.book, self.collection.books.all())
   ```

2. Execute os testes:
   ```bash
   python manage.py test
   ```

