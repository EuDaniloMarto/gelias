from django.shortcuts import get_object_or_404
from django.views.generic import CreateView

from CRM.clientes.models import Cliente

from .forms import EnderecoForm


class CriarEnderecosView(CreateView):
    template_name = "enderecos/criar_endereco.html"
    form_class = EnderecoForm
    cliente = None

    def get_cliente(self):
        if self.cliente:
            return self.cliente

        slug = self.kwargs.get("slug")

        if slug:
            self.cliente = get_object_or_404(Cliente, slug=slug)

        return self.cliente

    def get_context_data(self, **kwargs):
        self.extra_context = {
            "cliente": self.get_cliente(),
        }
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        cliente = self.get_cliente()
        self.success_url = cliente.ver_cliente()
        return super().get_success_url()

    def form_valid(self, form):
        cliente = self.get_cliente()
        self.object = form.save(commit=False)
        self.object.cliente = cliente
        self.object.save()
        return super().form_valid(form)


criar_endereco = CriarEnderecosView.as_view()
