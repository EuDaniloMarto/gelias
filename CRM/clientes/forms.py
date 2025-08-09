from django import forms

from .models import Cliente


class CriarClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = (
            "nome",
            "tipo_cliente",
            "alarme",
            "camera",
        )


class AtualizarClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = (
            "alarme",
            "camera",
            "ativo",
            "observacoes",
        )
