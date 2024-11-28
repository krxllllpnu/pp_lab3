from beaver_airlines.models import FlightReview, Flight, Passenger
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg, Count

class FlightReviewRepository:
    @staticmethod
    def get_average_rating_per_flight():
        return FlightReview.objects.values(
            'flight__flight_id',
            'flight__departure_airport__airport_name',
            'flight__arrival_airport__airport_name'
        ).annotate(
            avg_rating=Avg('rating'),
            review_count=Count('review_id')
        ).order_by('-avg_rating')

    @staticmethod
    def get_all():
        return FlightReview.objects.all()

    @staticmethod
    def get_by_id(review_id):
        try:
            return FlightReview.objects.get(pk=review_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create(flight_id, passenger_id, rating, comment, review_time):
        try:
            flight = Flight.objects.get(pk=flight_id)
            passenger = Passenger.objects.get(pk=passenger_id)
        except ObjectDoesNotExist:
            return None

        if not isinstance(rating, int) or not (1 <= rating <= 5):
            return None
        if not isinstance(comment, str):
            comment = ""

        review = FlightReview(flight=flight, passenger=passenger, rating=rating, comment=comment, review_time=review_time)
        review.save()
        return review

    @staticmethod
    def update(review_id, **kwargs):
        try:
            review = FlightReview.objects.get(pk=review_id)

            if 'rating' in kwargs and isinstance(kwargs['rating'], int) and 1 <= kwargs['rating'] <= 5:
                review.rating = kwargs['rating']
            if 'comment' in kwargs and isinstance(kwargs['comment'], str):
                review.comment = kwargs['comment']

            review.save()
            return review
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def delete(review_id):
        try:
            review = FlightReview.objects.get(pk=review_id)
            review.delete()
            return True
        except ObjectDoesNotExist:
            return False
