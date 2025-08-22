from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class TestRedirecionamentoPaginaInicial(TestCase):
    def test_status_code_302(self):
        resposta = self.client.get(reverse("crm:ir_para_lista_clientes"))
        self.assertEqual(resposta.status_code, HTTPStatus.FOUND)

    def test_redireciona_para_listar_clientes(self):
        resposta = self.client.get(reverse("crm:ir_para_lista_clientes"))
        self.assertRedirects(resposta, reverse("clientes:listar_clientes"))
