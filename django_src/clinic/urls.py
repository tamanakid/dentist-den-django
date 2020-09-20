from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()

# router.register('users', views.UserViewSet)
# router.register('groups', views.GroupViewSet)
router.register('patients', views.PatientViewSet)
# router.register('medications', views.MedicationViewSet)



urlpatterns = [
    path('', include(router.urls))
]
