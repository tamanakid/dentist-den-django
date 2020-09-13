from django.db import models
from django.contrib.auth.models import User

from clinic.models import Medication


class PatientType(models.IntegerChoices):
	__empty__ = "No definido"
	RES = 1, "Residencia"
	PED = 2, "Pediatría"
	ADU = 3, "Adultos"
	ESP = 4, "Especiales"


class Patient(models.Model):
	# personal information
	firstname = models.CharField(max_length=32)
	lastname_first = models.CharField(max_length=32)
	lastname_second = models.CharField(max_length=32, blank=True)
	email = models.EmailField(blank=True)

	# medical information
	date_birth = models.DateField(null=True)
	allergies = models.ManyToManyField(Medication, blank=True, related_name='allergic_patients')
	prescriptions = models.ManyToManyField(Medication, blank=True, related_name='prescriptions', through='ClinicPrescription')
	other_medication = models.ManyToManyField(Medication, blank=True, related_name='other_medication', through='OtherPrescription')


	# application-related information
	history_number = models.IntegerField(blank=False, null=False, unique=True)
	date_created = models.DateField(auto_now_add=True)
	# https://stackoverflow.com/questions/20203806/limit-maximum-choices-of-manytomanyfield
	current_professional = models.ManyToManyField(User, blank=True, related_name='patients')
	patient_type = models.IntegerField(choices=PatientType.choices, default=PatientType.__empty__)
	# notes_related

	def __str__(self):
		return f"{self.lastname_first}, {self.firstname}"

	@property
	def fullname(self):
		return f"{self.firstname} {self.lastname_first} {self.lastname_second}".rstrip()

	@property
	def initials(self):
		name = self.firstname[0]
		last1 = self.lastname_first[0]
		last2 = '' if self.lastname_second is None else self.lastname_second[0]
		return f"{name}{last1}{last2}"
