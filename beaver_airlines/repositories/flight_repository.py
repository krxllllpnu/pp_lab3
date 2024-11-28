from beaver_airlines.models import Flight
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Avg, ExpressionWrapper, F, DurationField

class FlightRepository:
    @staticmethod
    def get_average_flight_duration():
        result = Flight.objects.annotate(
            duration=ExpressionWrapper(
                F('arrival_time') - F('departure_time'),
                output_field=DurationField()
            )
        ).aggregate(avg_duration=Avg('duration'))
        return result

    @staticmethod
    def get_flight_durations():
        return Flight.objects.annotate(
            duration=ExpressionWrapper(
                F('arrival_time') - F('departure_time'),
                output_field=DurationField()
            )
        ).values('flight_id', 'duration').order_by('-duration')

    @staticmethod
    def get_flights_with_most_bookings():
        return Flight.objects.annotate(
            booking_count=Count('booking')
        ).filter(
            booking_count__gt=0
        ).order_by('-booking_count').values(
            'flight_id',
            'departure_airport__airport_name',
            'arrival_airport__airport_name',
            'booking_count'
        )

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