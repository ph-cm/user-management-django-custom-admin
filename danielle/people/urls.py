from django.urls import path, include
from people import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('people', views.PersonViewSet)
router.register('checkins', views.CheckinViewSet)
router.register('patient_companion_checkin', views.PatientCompanionCheckinViewSet)
router.register('home_services', views.HomeServicesViewSet)
router.register('professional_services', views.ProfessionalServicesViewSet)

urlpatterns = [
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('', include(router.urls)),
]