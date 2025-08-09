# SeuApp/factories.py
import factory

from CRM.clientes.models import Cliente


class ClienteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cliente

    # Defina os campos do seu modelo
    nome = factory.Faker("name")
    tipo_cliente = factory.Iterator(
        [
            Cliente.TipoCliente.PF,
            Cliente.TipoCliente.PJ,
        ]
    )
    ativo = factory.Faker("boolean")
    alarme = factory.Faker("boolean")
    camera = factory.Faker("boolean")
