from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify

from ..models import Cliente
from .factories import ClienteFactory


class ClienteModelTest(TestCase):
    def test_string_representacao(self):
        cliente = ClienteFactory()
        self.assertEqual(str(cliente), cliente.nome)

    def test_slug_eh_criado_automaticamente(self):
        cliente = ClienteFactory()
        expected_slug = slugify(cliente.nome)
        self.assertEqual(cliente.slug, expected_slug)

    def test_slug_nao_muda_quando_o_nome_eh_atualizado(self):
        cliente = ClienteFactory()
        original_slug = cliente.slug
        cliente.nome = f"{cliente.nome} Atualizado"
        cliente.save()
        self.assertEqual(cliente.slug, original_slug)

    def test_unique_constraint_on_nome(self):
        Cliente.objects.create(nome="Empresa de Teste")
        with self.assertRaises(Exception):
            Cliente.objects.create(nome="Empresa de Teste")

    def test_atualizar_cliente(self):
        cliente = ClienteFactory()
        expected_update_url = reverse(
            "clientes:atualizar_cliente", kwargs={"slug": cliente.slug}
        )
        self.assertEqual(cliente.atualizar_cliente(), expected_update_url)

    def test_ver_cliente(self):
        cliente = ClienteFactory()
        expected_view_url = reverse(
            "clientes:ver_cliente", kwargs={"slug": cliente.slug}
        )
        self.assertEqual(cliente.ver_cliente(), expected_view_url)

    def test_criar_cliente(self):
        cliente = ClienteFactory()
        expected_create_url = (
            f"{reverse('clientes:criar_cliente')}?from_cliente={cliente.slug}"
        )
        self.assertEqual(cliente.criar_cliente(), expected_create_url)
