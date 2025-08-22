from django.views import generic

from . import forms
from .models import Cliente


class CriarClientes(generic.CreateView):
    """View para criar clientes."""

    form_class = forms.FormularioCriarCliente
    template_name = "clientes/criar_cliente.html"

    def get_success_url(self):
        return self.object.ver_cliente()

    def get_context_data(self, **kwargs):
        cliente_anterior = self.request.GET.get("from_cliente")

        if cliente_anterior and "cliente_anterior" not in kwargs:
            kwargs["cliente_anterior"] = cliente_anterior

        return super().get_context_data(**kwargs)


criar_clientes = CriarClientes.as_view()


class ListarClientes(generic.ListView):
    """View para listar clientes."""

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
        return super().get_context_data(**kwargs)


listar_clientes = ListarClientes.as_view()


class VerCliente(generic.DetailView):
    """View para ver detalhes do cliente."""

    template_name = "clientes/ver_cliente.html"
    model = Cliente
    context_object_name = "cliente"

    def get_context_data(self, **kwargs):
        self.extra_context = {
            "dados": forms.FormularioVerCliente(instance=self.get_object()),
        }
        return super().get_context_data(**kwargs)


ver_cliente = VerCliente.as_view()


class AtualizarCliente(generic.UpdateView):
    """View para atualizar cliente."""

    template_name = "clientes/atualizar_cliente.html"
    form_class = forms.FormularioAtualizarCliente
    model = Cliente

    def get_success_url(self):
        return self.object.ver_cliente()


atualizar_cliente = AtualizarCliente.as_view()
