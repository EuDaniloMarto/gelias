from django import forms

from .models import Endereco


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = (
            "logradouro",
            "numero",
            "complemento",
            "bairro",
            "municipio",
            "estado",
            "cep",
        )

    def clean_cep(self):
        cep = self.cleaned_data.get("cep")
        if not cep.isdigit() or len(cep) != 8:
            raise forms.ValidationError("CEP deve conter 8 dígitos numéricos.")
        return cep
