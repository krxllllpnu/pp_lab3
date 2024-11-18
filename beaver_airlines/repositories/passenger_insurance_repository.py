from beaver_airlines.models import PassengerInsurance, Passenger
from django.core.exceptions import ObjectDoesNotExist

class PassengerInsuranceRepository:

    @staticmethod
    def get_all():
        return PassengerInsurance.objects.all()

    @staticmethod
    def get_by_id(passenger_id):
        try:
            return PassengerInsurance.objects.get(pk=passenger_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create(passenger_id, policy_number, coverage_amount, issue_date, expiry_date):
        try:
            passenger = Passenger.objects.get(pk=passenger_id)
        except ObjectDoesNotExist:
            return None

        if not isinstance(policy_number, str) or len(policy_number) > 50:
            return None
        if not isinstance(coverage_amount, float) or coverage_amount <= 0:
            return None

        insurance = PassengerInsurance(passenger=passenger, policy_number=policy_number, coverage_amount=coverage_amount,
                                       issue_date=issue_date, expiry_date=expiry_date)
        insurance.save()
        return insurance

    @staticmethod
    def update(passenger_id, **kwargs):
        try:
            insurance = PassengerInsurance.objects.get(pk=passenger_id)

            if 'policy_number' in kwargs and isinstance(kwargs['policy_number'], str) and len(kwargs['policy_number']) <= 50:
                insurance.policy_number = kwargs['policy_number']
            if 'coverage_amount' in kwargs and isinstance(kwargs['coverage_amount'], float) and kwargs['coverage_amount'] > 0:
                insurance.coverage_amount = kwargs['coverage_amount']
            if 'issue_date' in kwargs:
                insurance.issue_date = kwargs['issue_date']
            if 'expiry_date' in kwargs:
                insurance.expiry_date = kwargs['expiry_date']

            insurance.save()
            return insurance
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def delete(passenger_id):
        try:
            insurance = PassengerInsurance.objects.get(pk=passenger_id)
            insurance.delete()
            return True
        except ObjectDoesNotExist:
            return False
