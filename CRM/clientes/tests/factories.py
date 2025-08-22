import factory
from factory import fuzzy

from ..models import Cliente


class ClienteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cliente

    nome = fuzzy.FuzzyText(length=255)
    tipo_cliente = fuzzy.FuzzyChoice(choices=Cliente.TipoCliente.choices)
    ativo = fuzzy.FuzzyChoice(choices=[True, False])
    alarme = fuzzy.FuzzyChoice(choices=[True, False])
    camera = fuzzy.FuzzyChoice(choices=[True, False])
    observacoes = fuzzy.FuzzyChoice(choices=Cliente.TipoCliente.choices)
