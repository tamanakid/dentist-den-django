from django.db import models


class Prescription(models.Model):
	class Meta:
		abstract = True

	medication = models.ForeignKey('clinic.Medication', on_delete=models.CASCADE)
	patient = models.ForeignKey('clinic.Patient', on_delete=models.CASCADE)
	dose = models.CharField(max_length=32)


class ClinicPrescription(Prescription):
	# add appointment FK
	appointment = models.ForeignKey('clinic.Appointment', null=True, on_delete=models.SET_NULL, related_name="prescriptions")
	duration = models.CharField(max_length=32)
	frequency = models.CharField(max_length=32)
	indications = models.TextField(max_length=256)


class OtherPrescription(Prescription):
	pass
