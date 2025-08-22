from django.views.generic import RedirectView


class IrParaListaClientes(RedirectView):
    """
    Redireciona para a lista de clientes.
    """

    permanent = False
    pattern_name = "clientes:listar_clientes"


ir_para_lista_clientes = IrParaListaClientes.as_view()
