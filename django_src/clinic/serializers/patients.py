from rest_framework import serializers

from clinic.models import Patient


class PatientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Patient
		fields = ['fullname', 'date_birth']