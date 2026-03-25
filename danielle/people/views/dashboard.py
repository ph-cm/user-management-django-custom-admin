from django.shortcuts import render
from people.models import Person, Checkin, Checkout, HomeServices, ProfessionalServices


def dashboard_view(request):
    total_people = Person.objects.count()
    total_patients = Person.objects.filter(person_type="patient").count()
    total_companions = Person.objects.filter(person_type="companion").count()
    total_professionals = Person.objects.filter(person_type="professional").count()
    total_volunteers = Person.objects.filter(person_type="volunteer").count()

    active_checkins = Checkin.objects.filter(active=True).count()
    closed_checkins = Checkin.objects.filter(status="closed").count()
    total_checkouts = Checkout.objects.count()

    total_home_services = HomeServices.objects.count()
    total_professional_services = ProfessionalServices.objects.count()

    chemotherapy_count = Checkin.objects.filter(chemotherapy=True).count()
    radiotherapy_count = Checkin.objects.filter(radiotherapy=True).count()
    exams_count = Checkin.objects.filter(exams=True).count()
    with_companion_count = Checkin.objects.filter(companion__isnull=False).count()

    context = {
        "total_people": total_people,
        "total_patients": total_patients,
        "total_companions": total_companions,
        "total_professionals": total_professionals,
        "total_volunteers": total_volunteers,
        "active_checkins": active_checkins,
        "closed_checkins": closed_checkins,
        "total_checkouts": total_checkouts,
        "total_home_services": total_home_services,
        "total_professional_services": total_professional_services,
        "chemotherapy_count": chemotherapy_count,
        "radiotherapy_count": radiotherapy_count,
        "exams_count": exams_count,
        "with_companion_count": with_companion_count,
    }

    return render(request, "dashboard.html", context)