from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import AtualizarClienteForm, CriarClienteForm
from .models import Cliente


class CriarClientes(CreateView):
    form_class = CriarClienteForm
    template_name = "clientes/criar_cliente.html"

    def get_success_url(self):
        return self.object.ver_cliente()

    def get_context_data(self, **kwargs):
        cliente_anterior = self.request.GET.get("from_cliente")

        if cliente_anterior and "cliente_anterior" not in kwargs:
            kwargs["cliente_anterior"] = cliente_anterior

        return super().get_context_data(**kwargs)


criar_clientes = CriarClientes.as_view()


class ListarClientes(ListView):
    template_name = "clientes/listar_clientes.html"
    queryset = Cliente.objects.all().only(
        "nome", "tipo_cliente", "alarme", "camera", "ativo"
    )
    context_object_name = "clientes"
    paginate_by = 50

    def get_queryset(self):
        self.tipo_servico = self.kwargs.get("tipo_servico")

        if self.tipo_servico == "alarme":
            self.queryset = self.queryset.filter(alarme=True)
        elif self.tipo_servico == "camera":
            self.queryset = self.queryset.filter(camera=True)

        return super().get_queryset()

    def get_context_data(self, **kwargs):
        if "tipo_servico" not in kwargs:
            kwargs["tipo_servico"] = self.tipo_servico
            # import ipdb
            # ipdb.set_trace()
        return super().get_context_data(**kwargs)


listar_clientes = ListarClientes.as_view()


class VerCliente(DetailView):
    template_name = "clientes/ver_cliente.html"
    model = Cliente
    context_object_name = "cliente"


ver_cliente = VerCliente.as_view()


class AtualizarCliente(UpdateView):
    template_name = "clientes/atualizar_cliente.html"
    form_class = AtualizarClienteForm
    model = Cliente

    def get_success_url(self):
        return self.object.ver_cliente()


atualizar_cliente = AtualizarCliente.as_view()


class RemoverCliente(TemplateView):
    template_name = "clientes/remover_cliente.html"


remover_cliente = RemoverCliente.as_view()
