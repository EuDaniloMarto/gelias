from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class Index(LoginRequiredMixin, TemplateView):
    extra_context = {"pagina": "clientes"}
    template_name = "clientes/index.html"
