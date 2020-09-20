from rest_framework import serializers

from clinic.models import Patient


class PatientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Patient
		fields = ['id', 'fullname', 'date_birth']