from django.db import models
from .models_auth import DemandingParty, OfferingParty


MASK_TYPE = (
    ('0', 'FFP2'),
    ('1', 'FFP3'),
    ('2', 'Mouth Nose Proection'),

)


class MedicalEquipment(models.Model):
    pass


class Mask(MedicalEquipment):
    type = models.CharField(choices=MASK_TYPE)


DISINFECTANT_TYPE = (
    ('0', 'Virucidal'),
    ('1', 'Limited Virucidal'),
    ('2', '...')
)


class Disinfectant(MedicalEquipment):
    type = models.CharField(choices=DISINFECTANT_TYPE)


SPECIALIST_TYPES = (
    ('0', 'Nurse'),
    ('1', 'Family Doctor'),
    ('2', '...')
)


class Specialist(models.Model):
    type = models.CharField(choices=SPECIALIST_TYPES, max_length=2)
    name = models.CharField()


# -----------------------------------------------------------------------------------------


class MedicalEquipmentDemand(models.Model):
    demanding_party = models.ForeignKey(DemandingParty, on_delete=models.CASCADE)
    resource = models.ForeignKey(MedicalEquipment, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class SpecialistDemand(models.Model):
    demanding_party = models.ForeignKey(DemandingParty, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()


class MedicalEquipmentOffer(models.Model):
    offering_party = models.ForeignKey(OfferingParty, on_delete=models.CASCADE)
    resource = models.ForeignKey(MedicalEquipment, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class SpecialistOffer(models.Model):
    offering_party = models.ForeignKey(OfferingParty, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
