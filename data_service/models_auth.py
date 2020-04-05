from django.db import models
from django.contrib.auth.models import User


class PandaLogicaAccount(models.Model):
    class Meta:
        abstract = True

    address = models.CharField()
    zip = models.CharField()
    user = models.OneToOneField(User, on_delete=models.PROTECT)


class OfferingParty(models.Model):
    class Meta:
        abstract = True


class DemandingParty(models.Model):
    class Meta:
        abstract = True


# -----------------------------------------------------------------------------------------


class PrivatePractitioner(PandaLogicaAccount, DemandingParty):
    zsr_number = models.CharField()
    # he can place only demands


class ThirdPartySupplier(PandaLogicaAccount, OfferingParty):
    name = models.CharField()
    certified = models.BooleanField(default=False)
    # he can place only offers


class Hospital(PandaLogicaAccount, DemandingParty, OfferingParty):
    gln_number = models.CharField()
    # he can place both offers and demands
