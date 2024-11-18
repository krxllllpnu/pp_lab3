from rest_framework import serializers
from .models import Airplane, Airport, CrewMember, Flight, FlightReview, Passenger, Booking, PassengerInsurance

class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = '__all__'

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'

class CrewMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrewMember
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class FlightReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightReview
        fields = '__all__'

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class PassengerInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerInsurance
        fields = '__all__'