from beaver_airlines.models import Passenger
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count

class PassengerRepository:
    @staticmethod
    def get_passengers_with_most_bookings():
        return Passenger.objects.annotate(
            booking_count=Count('booking')
        ).values(
            'passenger_id', 'first_name', 'last_name', 'email', 'phone', 'booking_count'
        ).order_by('-booking_count')

    @staticmethod
    def get_all():
        return Passenger.objects.all()

    @staticmethod
    def get_by_id(passenger_id):
        try:
            return Passenger.objects.get(pk=passenger_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create(first_name, last_name, email, phone):
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            return None
        if not isinstance(email, str) or "@" not in email:
            return None
        if not isinstance(phone, str) or not phone.isdigit():
            return None

        passenger = Passenger(first_name=first_name, last_name=last_name, email=email, phone=phone)
        passenger.save()
        return passenger

    @staticmethod
    def update(passenger_id, **kwargs):
        try:
            passenger = Passenger.objects.get(pk=passenger_id)

            if 'first_name' in kwargs and isinstance(kwargs['first_name'], str):
                passenger.first_name = kwargs['first_name']
            if 'last_name' in kwargs and isinstance(kwargs['last_name'], str):
                passenger.last_name = kwargs['last_name']
            if 'email' in kwargs and isinstance(kwargs['email'], str) and "@" in kwargs['email']:
                passenger.email = kwargs['email']
            if 'phone' in kwargs and isinstance(kwargs['phone'], str) and kwargs['phone'].isdigit():
                passenger.phone = kwargs['phone']

            passenger.save()
            return passenger
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def delete(passenger_id):
        try:
            passenger = Passenger.objects.get(pk=passenger_id)
            passenger.delete()
            return True
        except ObjectDoesNotExist:
            return False
