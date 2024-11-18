from beaver_airlines.models import Airport
from django.core.exceptions import ObjectDoesNotExist

class AirportRepository:

        @staticmethod
        def get_all():
            return Airport.objects.all()

        @staticmethod
        def get_by_id(airport_id):
            try:
                return Airport.objects.get(pk=airport_id)
            except ObjectDoesNotExist:
                return None

        @staticmethod
        def create(airport_name, city, country):
            airport = Airport(airport_name=airport_name, city=city, country=country)
            airport.save()
            return airport

        @staticmethod
        def update(airport_id, **kwargs):
            try:
                airport = Airport.objects.get(pk=airport_id)
                for key, value in kwargs.items():
                    setattr(airport, key, value)
                airport.save()
                return airport
            except ObjectDoesNotExist:
                return None

        @staticmethod
        def delete(airport_id):
            try:
                airport = Airport.objects.get(pk=airport_id)
                airport.delete()
                return True
            except ObjectDoesNotExist:
                return False