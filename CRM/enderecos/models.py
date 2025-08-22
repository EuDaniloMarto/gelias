from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

cep_validator = RegexValidator(
    regex=r"^\d{8}$", message="O CEP deve conter 8 dígitos.", code="invalid_cep"
)


class Endereco(models.Model):
    class Estado(models.TextChoices):
        AC = "AC", _("Acre")
        AL = "AL", _("Alagoas")
        AP = "AP", _("Amapá")
        AM = "AM", _("Amazonas")
        BA = "BA", _("Bahia")
        CE = "CE", _("Ceará")
        DF = "DF", _("Distrito Federal")
        ES = "ES", _("Espírito Santo")
        GO = "GO", _("Goiás")
        MA = "MA", _("Maranhão")
        MT = "MT", _("Mato Grosso")
        MS = "MS", _("Mato Grosso do Sul")
        MG = "MG", _("Minas Gerais")
        PA = "PA", _("Pará")
        PB = "PB", _("Paraíba")
        PR = "PR", _("Paraná")
        PE = "PE", _("Pernambuco")
        PI = "PI", _("Piauí")
        RJ = "RJ", _("Rio de Janeiro")
        RN = "RN", _("Rio Grande do Norte")
        RS = "RS", _("Rio Grande do Sul")
        RO = "RO", _("Rondônia")
        RR = "RR", _("Roraima")
        SC = "SC", _("Santa Catarina")
        SP = "SP", _("São Paulo")
        SE = "SE", _("Sergipe")
        TO = "TO", _("Tocantins")

    criado_em = models.DateTimeField(_("Criado em"), auto_now_add=True)
    atualizado_em = models.DateTimeField(_("Atualizado em"), auto_now=True)
    cliente = models.ForeignKey(
        "clientes.Cliente",
        verbose_name=_("Cliente"),
        on_delete=models.CASCADE,
        related_name="enderecos",
    )
    logradouro = models.CharField(_("Logradouro"), max_length=255)
    numero = models.CharField(_("Número"), max_length=10, blank=True)
    complemento = models.CharField(_("Complemento"), max_length=100, blank=True)
    bairro = models.CharField(_("Bairro"), max_length=100, blank=True)
    municipio = models.CharField(_("Município"), max_length=100, blank=True)
    estado = models.CharField(
        _("Estado"), max_length=2, choices=Estado.choices, default=Estado.SP
    )
    cep = models.CharField(
        _("CEP"),
        max_length=10,
        blank=True,
        validators=[cep_validator],
        help_text=_("Escreva o CEP sem traços ou espaços. Exemplo: 12345678."),
    )

    class Meta:
        verbose_name = _("Endereço")
        verbose_name_plural = _("Endereços")
        ordering = [
            "estado",
            "municipio",
            "bairro",
            "logradouro",
            "numero",
        ]

    def __str__(self):
        """Representação no padrão Google: "logradouro, número - complemento, bairro, município - estado, CEP"""

        address = f"{self.logradouro}, {self.numero}"

        if self.complemento:
            address += f" - {self.complemento}"
        address += f", {self.bairro}, {self.municipio} - {self.estado}, {self.cep}"

        return address
