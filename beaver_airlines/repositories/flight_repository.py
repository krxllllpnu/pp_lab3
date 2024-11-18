from beaver_airlines.models import Flight
from django.core.exceptions import ObjectDoesNotExist

class FlightRepository:

    @staticmethod
    def get_all():
        return Flight.objects.all()

    @staticmethod
    def get_by_id(flight_id):
        try:
            return Flight.objects.get(pk=flight_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create(airplane, departure_airport, arrival_airport, departure_time, arrival_time):
        flight = Flight(airplane=airplane, departure_airport=departure_airport, arrival_airport=arrival_airport, departure_time=departure_time, arrival_time=arrival_time)
        flight.save()
        return flight

    @staticmethod
    def update(flight_id, **kwargs):
        try:
            flight = Flight.objects.get(pk=flight_id)
            for key, value in kwargs.items():
                setattr(flight, key, value)
            flight.save()
            return flight
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def delete(flight_id):
        try:
            flight = Flight.objects.get(pk=flight_id)
            flight.delete()
            return True
        except ObjectDoesNotExist:
            return False