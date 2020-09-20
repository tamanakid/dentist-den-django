from rest_framework import viewsets

from clinic.models import Patient
from clinic.serializers import PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
	queryset = Patient.objects.all()
	serializer_class = PatientSerializer

	def get_queryset(self):
		user = self.request.user
		return user.patients.all()
