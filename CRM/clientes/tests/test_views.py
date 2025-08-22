from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from ..models import Cliente
from .factories import ClienteFactory


class CrieClientesViewTests(TestCase):
    def setUp(self):
        self.url = reverse("clientes:criar_cliente")

    def test_requisicao_GET_com_status_200(self):
        resposta = self.client.get(self.url)
        self.assertEqual(resposta.status_code, HTTPStatus.OK)

    def test_nome_template_usado(self):
        resposta = self.client.get(self.url)
        self.assertTemplateUsed(resposta, "clientes/criar_cliente.html")

    def test_cliente_eh_criado_com_sucesso(self):
        data = {
            "nome": "João Doe",
            "tipo_cliente": Cliente.TipoCliente.PF,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(Cliente.objects.count(), 1)

    def test_codigo_de_status_apos_criar_um_cliente_eh_302(self):
        data = {
            "nome": "João Doe",
            "tipo_cliente": Cliente.TipoCliente.PF,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_redireciona_para_a_pagina_de_detalhes_apos_criar_cliente(self):
        data = {
            "nome": "João Doe",
            "tipo_cliente": Cliente.TipoCliente.PF,
        }
        response = self.client.post(self.url, data)
        cliente = Cliente.objects.first()
        self.assertRedirects(response, cliente.ver_cliente())


class TestCaseListarCliente(TestCase):
    def test_status_code_ok(self):
        request = self.client.get(reverse("clientes:listar_clientes"))
        self.assertEqual(request.status_code, HTTPStatus.OK)

    def test_template_name_(self):
        request = self.client.get(reverse("clientes:listar_clientes"))
        self.assertTemplateUsed(request, "clientes/listar_clientes.html")


class TestCaseVerCliente(TestCase):
    def test_status_code_ok(self):
        cliente = ClienteFactory()
        request = self.client.get(cliente.ver_cliente())
        self.assertEqual(request.status_code, HTTPStatus.OK)

    def test_template_name_(self):
        cliente = ClienteFactory()
        request = self.client.get(cliente.ver_cliente())
        self.assertTemplateUsed(request, "clientes/ver_cliente.html")


class TestCaseAtualizarCliente(TestCase):
    def test_status_code_ok(self):
        cliente = ClienteFactory()
        request = self.client.get(cliente.atualizar_cliente())
        self.assertEqual(request.status_code, HTTPStatus.OK)

    def test_template_name_(self):
        cliente = ClienteFactory()
        request = self.client.get(cliente.atualizar_cliente())
        self.assertTemplateUsed(request, "clientes/atualizar_cliente.html")
