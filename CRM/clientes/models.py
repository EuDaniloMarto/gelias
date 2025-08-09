from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Cliente(models.Model):
    class TipoCliente(models.TextChoices):
        PF = "PF", _("Pessoa Física")
        PJ = "PJ", _("Pessoa Jurídica")

    criado_em = models.DateTimeField(_("Criado em"), auto_now_add=True)
    atualizado_em = models.DateTimeField(_("Atualizado em"), auto_now=True)
    nome = models.CharField(_("Nome"), max_length=255, unique=True)
    slug = models.SlugField(_("Slug"), unique=True, max_length=255)
    tipo_cliente = models.CharField(
        _("Tipo de Cliente"),
        max_length=2,
        choices=TipoCliente.choices,
        default=TipoCliente.PF,
    )
    observacoes = models.TextField(_("Observações"), blank=True)
    ativo = models.BooleanField(
        _("Ativo"),
        help_text=_("Desmarque essa opção caso o cliente cancele o serviço."),
        default=True,
    )
    alarme = models.BooleanField(
        _("Alarme"),
        help_text=_(
            "Marque essa opção caso o serviço de monitoramento por alarme tenha sido contratado."
        ),
        default=False,
    )
    camera = models.BooleanField(
        _("Câmera"),
        help_text=_(
            "Marque essa opção caso o serviço de monitoramento por câmeras tenha sido contratado."
        ),
        default=False,
    )

    @property
    def listar_enderecos(self):
        return self.enderecos.all()

    class Meta:
        verbose_name = _("Cliente")
        verbose_name_plural = _("Clientes")
        ordering = [
            "nome",
            "ativo",
        ]
        indexes = [models.Index(fields=["nome"], name="idx_cliente_nome")]

    def __str__(self):
        return self.nome

    def atualizar_cliente(self):
        return reverse("clientes:atualizar_cliente", kwargs={"slug": self.slug})

    def ver_cliente(self):
        return reverse("clientes:ver_cliente", kwargs={"slug": self.slug})

    def criar_cliente(self):
        return f"{reverse('clientes:criar_cliente')}?from_cliente={self.slug}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)


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
    cep = models.CharField(_("CEP"), max_length=10, blank=True)

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
        """Retorna uma representação legível do endereço."""
        return f"{self.logradouro}, {self.numero}. {self.bairro}. {self.municipio}/{self.estado}"


class Dvr(models.Model):
    criado_em = models.DateTimeField(_("Criado em"), auto_now_add=True)
    atualizado_em = models.DateTimeField(_("Atualizado em"), auto_now=True)
    cliente = models.ForeignKey(
        "clientes.Cliente",
        verbose_name=_("Cliente"),
        on_delete=models.CASCADE,
        related_name="DVR",
    )
    fabricante = models.CharField(_("Fabricante"), max_length=32, blank=True)
    modelo = models.CharField(_("Modelo"), max_length=32, blank=True)
    serial = models.CharField(_("Serial"), max_length=64, blank=True)
    ip = models.CharField(_("IP"), max_length=32, blank=True)
    porta = models.CharField(_("Porta"), max_length=10, blank=True)
    usuario = models.CharField(_("Usuário"), max_length=64, blank=True)
    senha = models.CharField(_("Senha"), max_length=255, blank=True)

    class Meta:
        verbose_name = _("DVR")
        verbose_name_plural = _("DVR")
        ordering = [
            "fabricante",
            "modelo",
        ]


class CentralAlarme(models.Model):
    criado_em = models.DateTimeField(_("Criado em"), auto_now_add=True)
    atualizado_em = models.DateTimeField(_("Atualizado em"), auto_now=True)
    cliente = models.ForeignKey(
        "clientes.Cliente",
        verbose_name=_("Cliente"),
        on_delete=models.CASCADE,
        related_name="centrais_de_alarmes",
    )
    mac = models.CharField(_("MAC"), max_length=64, blank=True)
    usuario = models.CharField(_("Usuário"), max_length=64, blank=True)
    senha = models.CharField(_("Senha"), max_length=255, blank=True)

    class Meta:
        verbose_name = _("Central de Alarme")
        verbose_name_plural = _("Centrais de Alarmes")
        ordering = [
            "mac",
        ]
