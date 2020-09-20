from django.db import models
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError


class Appointment(models.Model):
	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['date', 'patient'], name="unique_date_for_patient")
		]

	patient = models.ForeignKey('clinic.Patient', related_name="appointments", on_delete=models.CASCADE)
	professionals = models.ManyToManyField('auth.User', through='AppointmentProfessionalRelationship')
	
	date = models.ForeignKey('clinic.Date', on_delete=models.PROTECT)

	associated_appointments = models.ManyToManyField('self', blank=True)
	description = models.TextField(max_length=256)
	comments = models.TextField(max_length=256)


class AppointmentTreatments(models.Model):
	appointment = models.ForeignKey('clinic.Appointment', null=False, related_name="treatments", on_delete=models.CASCADE)
	description = models.CharField(max_length=256)


class AppointmentProfessionalRelationship(models.Model):
	professional = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	appointment = models.ForeignKey('clinic.Appointment', on_delete=models.CASCADE)
	creator = models.BooleanField(default=False)


def unique_date_for_professional(sender, instance, **kwargs):
    if instance.professionals.count() > 3:
        raise ValidationError("An appointment cannot be attended by more than three professionals")


m2m_changed.connect(unique_date_for_professional, sender=Appointment.professionals.through)