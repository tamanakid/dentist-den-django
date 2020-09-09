from django.db import models
from django.contrib.auth.models import User


class PatientType(models.IntegerChoices):
	__empty__ = "No definido"
	RES = 1, "Residencia"
	PED = 2, "Pediatría"
	ADU = 3, "Adultos"


class Patient(models.Model):
	# personal information
	firstname = models.CharField(max_length=32)
	lastname_first = models.CharField(max_length=32)
	lastname_second = models.CharField(max_length=32, blank=True)

	# medical information
	date_birth = models.DateField(null=True)
	# allergies = models.ManyToManyField(Medication, blank=True, related_name="allergic_patients")

	# application-related information
	date_created = models.DateField(auto_now_add=True)
	# https://stackoverflow.com/questions/20203806/limit-maximum-choices-of-manytomanyfield
	current_professional = models.ManyToManyField(User, blank=True, related_name='patients')
	patient_type = models.IntegerField(choices=PatientType.choices, default=PatientType.__empty__)
	# notes_related

	def __str__(self):
		return f"{self.lastname_first}, {self.firstname}"
