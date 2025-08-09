from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from .factories import ClienteFactory


class TestCaseCriarCliente(TestCase):
    def test_status_code_ok(self):
        request = self.client.get(reverse("clientes:criar_cliente"))
        self.assertEqual(request.status_code, HTTPStatus.OK)

    def test_template_name_(self):
        request = self.client.get(reverse("clientes:criar_cliente"))
        self.assertTemplateUsed(request, "clientes/criar_cliente.html")


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
        request = self.client.get(
            reverse("clientes:ver_cliente", kwargs={"slug": cliente.slug})
        )
        self.assertEqual(request.status_code, HTTPStatus.OK)

    def test_template_name_(self):
        cliente = ClienteFactory()
        request = self.client.get(
            reverse("clientes:ver_cliente", kwargs={"slug": cliente.slug})
        )
        self.assertTemplateUsed(request, "clientes/ver_cliente.html")


class TestCaseAtualizarCliente(TestCase):
    def test_status_code_ok(self):
        cliente = ClienteFactory()
        request = self.client.get(
            reverse("clientes:atualizar_cliente", kwargs={"slug": cliente.slug})
        )
        self.assertEqual(request.status_code, HTTPStatus.OK)

    def test_template_name_(self):
        cliente = ClienteFactory()
        request = self.client.get(
            reverse("clientes:atualizar_cliente", kwargs={"slug": cliente.slug})
        )
        self.assertTemplateUsed(request, "clientes/atualizar_cliente.html")
