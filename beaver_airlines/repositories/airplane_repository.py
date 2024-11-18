from beaver_airlines.models import Airplane
from django.core.exceptions import ObjectDoesNotExist

class AirplaneRepository:

    @staticmethod
    def get_all():
        return Airplane.objects.all()

    @staticmethod
    def get_by_id(airplane_id):
        try:
            return Airplane.objects.get(pk=airplane_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create(manufacturer, model, capacity):
        airplane = Airplane(manufacturer=manufacturer, model=model, capacity=capacity)
        airplane.save()
        return airplane

    @staticmethod
    def update(airplane_id, **kwargs):
        try:
            airplane = Airplane.objects.get(pk=airplane_id)
            for key, value in kwargs.items():
                setattr(airplane, key, value)
            airplane.save()
            return airplane
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def delete(airplane_id):
        try:
            airplane = Airplane.objects.get(pk=airplane_id)
            airplane.delete()
            return True
        except ObjectDoesNotExist:
            return False
