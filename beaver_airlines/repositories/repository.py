from .airplane_repository import AirplaneRepository
from .airport_repository import AirportRepository
from .booking_repository import BookingRepository
from .crew_member_repository import CrewMemberRepository
from .flight_repository import FlightRepository
from .flight_review_repository import FlightReviewRepository
from .passenger_repository import PassengerRepository
from .passenger_insurance_repository import PassengerInsuranceRepository

class Repository:

    @staticmethod
    def airplanes():
        return AirplaneRepository()

    @staticmethod
    def airports():
        return AirportRepository()

    @staticmethod
    def bookings():
        return BookingRepository()

    @staticmethod
    def crew_members():
        return CrewMemberRepository()

    @staticmethod
    def flights():
        return FlightRepository()

    @staticmethod
    def flight_reviews():
        return FlightReviewRepository()

    @staticmethod
    def passengers():
        return PassengerRepository()

    @staticmethod
    def passenger_insurance():
        return PassengerInsuranceRepository()