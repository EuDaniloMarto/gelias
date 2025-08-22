from django import forms

from .models import Cliente


class FormulárioBase(forms.ModelForm):
    """Base para formulários de cliente."""

    class Meta:
        model = Cliente
        fields = (
            "nome",
            "tipo_cliente",
            "alarme",
            "camera",
            "ativo",
            "observacoes",
        )


class FormularioCriarCliente(FormulárioBase):
    """Formulário para criar um novo cliente."""

    pass


class FormularioAtualizarCliente(FormulárioBase):
    """Formulário para atualizar um cliente existente."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in ["nome", "tipo_cliente"]:
            self.fields[field].widget.attrs["readonly"] = "readonly"


class FormularioVerCliente(FormulárioBase):
    """Formulário para visualizar os detalhes de um cliente."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["disabled"] = "disabled"
