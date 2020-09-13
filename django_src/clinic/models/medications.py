from django.db import models


class Medication(models.Model):
	name = models.CharField(max_length=64)
