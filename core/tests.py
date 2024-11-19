from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Colecao, Livro, Autor, Categoria

class ColecaoTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.autor = Autor.objects.create(nome='Autor Teste')
        self.categoria = Categoria.objects.create(nome='Categoria Teste')
        self.livro = Livro.objects.create(titulo='Livro Teste', autor=self.autor, categoria=self.categoria, publicado_em='2024-01-01')

    def test_create_colecao(self):
        response = self.client.post('/colecoes/', {'nome': 'Minha Coleção', 'descricao': 'Descrição da coleção', 'livros': [self.livro.id]})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Colecao.objects.count(), 1)
        self.assertEqual(Colecao.objects.get().nome, 'Minha Coleção')

    def test_only_owner_can_edit_colecao(self):
        colecao = Colecao.objects.create(nome='Coleção Teste', colecionador=self.user)
        response = self.client.put(f'/colecoes/{colecao.id}/', {'nome': 'Coleção Editada'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Colecao.objects.get().nome, 'Coleção Editada')