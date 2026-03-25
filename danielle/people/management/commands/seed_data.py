from django.core.management.base import BaseCommand
from people.models import (
    Person,
    Checkin,
    Checkout,
    HomeServices,
    ProfessionalServices,
    PatientCompanionCheckin,
)


class Command(BaseCommand):
    help = "Popula o banco com dados de teste"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Limpando dados antigos..."))

        Checkout.objects.all().delete()
        HomeServices.objects.all().delete()
        ProfessionalServices.objects.all().delete()
        PatientCompanionCheckin.objects.all().delete()
        Checkin.objects.all().delete()
        Person.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Banco limpo."))

       
        paciente1 = Person.objects.create(
            name="Pedro Henrique",
            person_type="patient",
            gender="M",
            state="MG",
            city="Araguari"
        )

        paciente2 = Person.objects.create(
            name="Maria Clara",
            person_type="patient",
            gender="F",
            state="MG",
            city="Uberlandia"
        )

        acompanhante = Person.objects.create(
            name="Ana Paula",
            person_type="companion",
            gender="F",
            state="MG",
            city="Uberlandia"
        )

        profissional = Person.objects.create(
            name="Dr. Paulo Lima",
            person_type="professional",
            gender="M",
            state="MG",
            city="Araguari"
        )

        voluntario = Person.objects.create(
            name="Carla Mendes",
            person_type="volunteer",
            gender="F",
            state="MG",
            city="Araguari"
        )

        self.stdout.write(self.style.SUCCESS("Pessoas criadas."))

       
        checkin1 = Checkin.objects.create(
            person=paciente1,
            reason="patient",
            active=True,
            status="open",
            chemotherapy=True
        )

        checkin2 = Checkin.objects.create(
            person=paciente2,
            reason="patient",
            companion=acompanhante,
            active=True,
            status="open",
            exams=True
        )

        checkin3 = Checkin.objects.create(
            person=profissional,
            reason="professional",
            active=True,
            status="open"
        )

        self.stdout.write(self.style.SUCCESS("Check-ins criados."))

        checkout = Checkout.objects.create(checkin=checkin2)

        self.stdout.write(self.style.SUCCESS("Checkout criado."))

        HomeServices.objects.create(
            person=paciente1,
            breakfast=True,
            lunch=True,
            dinner=True,
            sleep=True
        )

        HomeServices.objects.create(
            person=paciente2,
            breakfast=True,
            shower=True,
            sleep=True
        )

       
        ProfessionalServices.objects.create(
            professional=profissional,
            title="Atendimento psicológico",
            description="Sessão inicial com paciente"
        )

        self.stdout.write(self.style.SUCCESS("Serviços criados."))

        self.stdout.write(self.style.SUCCESS("Seed finalizada com sucesso!"))