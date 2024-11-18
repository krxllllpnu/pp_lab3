from beaver_airlines.models import Booking, Flight, Passenger
from django.core.exceptions import ObjectDoesNotExist

class BookingRepository:

    @staticmethod
    def get_all():
        return Booking.objects.all()

    @staticmethod
    def get_by_id(booking_id):
        try:
            return Booking.objects.get(pk=booking_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create(flight_id, passenger_id, seat_number, booking_time):
        try:
            flight = Flight.objects.get(pk=flight_id)
            passenger = Passenger.objects.get(pk=passenger_id)
        except ObjectDoesNotExist:
            return None

        if not isinstance(seat_number, str) or len(seat_number) > 6:
            return None

        booking = Booking(flight=flight, passenger=passenger, seat_number=seat_number, booking_time=booking_time)
        booking.save()
        return booking

    @staticmethod
    def update(booking_id, **kwargs):
        try:
            booking = Booking.objects.get(pk=booking_id)

            if 'seat_number' in kwargs and isinstance(kwargs['seat_number'], str) and len(kwargs['seat_number']) <= 6:
                booking.seat_number = kwargs['seat_number']
            if 'booking_time' in kwargs:
                booking.booking_time = kwargs['booking_time']

            booking.save()
            return booking
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def delete(booking_id):
        try:
            booking = Booking.objects.get(pk=booking_id)
            booking.delete()
            return True
        except ObjectDoesNotExist:
            return False
