from django.db import models

from clinic.models import Patient, Medication



class Prescription(models.Model):
	class Meta:
		abstract = True

	medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	dose = models.CharField(max_length=32)


class ClinicPrescription(Prescription):
	# add appointment FK
	duration = models.CharField(max_length=32)
	frequency = models.CharField(max_length=32)
	indications = models.TextField(max_length=256)


class OtherPrescription(Prescription):
	pass
