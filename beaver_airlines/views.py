from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .repositories import Repository
from .serializers import AirplaneSerializer, AirportSerializer, CrewMemberSerializer, FlightSerializer, FlightReviewSerializer, PassengerSerializer, BookingSerializer, PassengerInsuranceSerializer

from django.contrib.auth import login
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

def is_admin(user):
    return user.is_staff

@login_required
def add_passenger(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        passenger = Repository.passengers().create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone
        )

        return redirect('add_insurance', passenger_id=passenger.passenger_id)

    return render(request, 'add_passenger.html')

@login_required
def add_insurance(request, passenger_id):
    if request.method == 'POST':
        policy_number = request.POST.get('policy_number')
        coverage_amount = request.POST.get('coverage_amount')
        issue_date = request.POST.get('issue_date')
        expiry_date = request.POST.get('expiry_date')

        passenger = Repository.passengers().get_by_id(passenger_id)

        Repository.passenger_insurance().create(
            passenger=passenger.passenger_id,
            policy_number=policy_number,
            coverage_amount=coverage_amount,
            issue_date=issue_date,
            expiry_date=expiry_date
        )

        return redirect('booking_form')

    return render(request, 'add_insurance.html', {'passenger_id': passenger_id})

@login_required
def booking_form(request):
    if request.method == 'POST':
        departure_airport_id = request.POST.get('departure_airport')
        arrival_airport_id = request.POST.get('arrival_airport')
        flight_id = request.POST.get('flight')
        passenger_id = request.POST.get('passenger_id')
        seat_number = request.POST.get('seat_number')

        try:
            departure_airport = Repository.airports().get_by_id(departure_airport_id)
            arrival_airport = Repository.airports().get_by_id(arrival_airport_id)
            passenger = Repository.passengers().get_by_id(passenger_id)

            flight = Repository.flights().get_by_id(flight_id)

            if not flight:
                return render(request, 'booking_form.html', {'error': 'No suitable flight found'})

            Repository.bookings().create(
                flight.flight_id,
                passenger.passenger_id,
                seat_number=seat_number,
                booking_time=timezone.now()
            )

            messages.success(request, "Booking successfully created.")
            return redirect('booking_list')

        except ObjectDoesNotExist:
            return render(request, 'booking_form.html', {'error': 'No data found'})

    passengers = Repository.passengers().get_all().filter(email=request.user.email)
    airports = Repository.airports().get_all()
    return render(request, 'booking_form.html', {'airports': airports, 'passengers': passengers})

from django.http import JsonResponse

@login_required
def get_available_flights(request, departure_airport_id, arrival_airport_id):
    if not departure_airport_id or not arrival_airport_id:
        return JsonResponse([], safe=False)

    flights = Repository.flights().get_all().filter(
        departure_airport_id=departure_airport_id,
        arrival_airport_id=arrival_airport_id
    ).values('flight_id', 'departure_time', 'arrival_time')

    return JsonResponse(list(flights), safe=False)

@login_required
def booking_list(request):
    if request.user.is_staff:
        bookings = Repository.bookings().get_all()
    else:
        bookings = Repository.bookings().get_all().filter(passenger__email=request.user.email)

    return render(request, 'booking_list.html', {'bookings': bookings})

from django.http import HttpResponseForbidden
from django.contrib import messages

@login_required
def booking_detail(request, booking_id):
    booking = Repository.bookings().get_by_id(booking_id)
    if not request.user.is_staff and booking.passenger.email != request.user.email:
        return HttpResponseForbidden("You do not have access to this booking.")

    return render(request, 'booking_detail.html', {'booking': booking})

@login_required
def delete_booking(request, booking_id):
    booking = Repository.bookings().get_by_id(booking_id)

    try:
        passenger = Repository.passengers().get_by_id(booking.passenger.passenger_id)
    except Repository.passengers().get_by_id(booking.passenger.passenger_id).DoesNotExist:
        messages.error(request, "The passenger associated with the booking was not found.")
        return redirect('booking_list')

    if request.user.email != passenger.email and not request.user.is_superuser:
        messages.error(request, "You do not have the right to delete this booking.")
        return redirect('booking_list')

    Repository.bookings().delete(booking_id)
    messages.success(request, "Booking successfully deleted.")
    return redirect('booking_list')

@login_required
def confirm_delete_booking(request, booking_id):
    booking = Repository.bookings().get_by_id(booking_id)
    return render(request, 'confirm_delete.html', {'booking': booking})

@api_view(['GET'])
@login_required
@user_passes_test(is_admin)
def get_airplanes(request):
    airplanes = Repository.airplanes().get_all()
    serializer = AirplaneSerializer(airplanes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@login_required
@user_passes_test(is_admin)
def get_airplane(request, airplane_id):
    airplane = Repository.airplanes().get_by_id(airplane_id)
    if airplane is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AirplaneSerializer(airplane)
    return Response(serializer.data)

@api_view(['POST'])
@login_required
@user_passes_test(is_admin)
def create_airplane(request):
    manufacturer = request.data.get('manufacturer')
    model = request.data.get('model')
    capacity = request.data.get('capacity')
    if manufacturer is None or model is None or capacity is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    airplane = Repository.airplanes().create(manufacturer, model, capacity)
    if airplane is None:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    serializer = AirplaneSerializer(airplane)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@login_required
@user_passes_test(is_admin)
def update_airplane(request, airplane_id):
    airplane = Repository.airplanes().get_by_id(airplane_id)
    if airplane is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    manufacturer = request.data.get('manufacturer')
    model = request.data.get('model')
    capacity = request.data.get('capacity')
    if manufacturer is not None:
        airplane.manufacturer = manufacturer
    if model is not None:
        airplane.model = model
    if capacity is not None:
        airplane.capacity = capacity
    airplane = Repository.airplanes().update(airplane_id, manufacturer=manufacturer, model=model, capacity=capacity)
    if airplane is None:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    serializer = AirplaneSerializer(airplane)
    return Response(serializer.data)

@api_view(['DELETE'])
@login_required
@user_passes_test(is_admin)
def delete_airplane(request, airplane_id):
    airplane = Repository.airplanes().get_by_id(airplane_id)
    if airplane is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if not Repository.airplanes().delete(airplane_id):
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@login_required
@user_passes_test(is_admin)
def get_airports(request):
    airports = Repository.airports().get_all()
    serializer = AirportSerializer(airports, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@login_required
@user_passes_test(is_admin)
def get_airport(request, airport_id):
    airport = Repository.airports().get_by_id(airport_id)
    if airport is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AirportSerializer(airport)
    return Response(serializer.data)

@api_view(['POST'])
@login_required
@user_passes_test(is_admin)
def create_airport(request):
    airport_name = request.data.get('airport_name')
    city = request.data.get('city')
    country = request.data.get('country')
    if airport_name is None or city is None or country is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    airport = Repository.airports().create(airport_name, city, country)
    if airport is None:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    serializer = AirportSerializer(airport)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@login_required
@user_passes_test(is_admin)
def update_airport(request, airport_id):
    airport = Repository.airports().get_by_id(airport_id)
    if airport is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    airport_name = request.data.get('airport_name')
    city = request.data.get('city')
    country = request.data.get('country')
    if airport_name is not None:
        airport.airport_name = airport_name
    if city is not None:
        airport.city = city
    if country is not None:
        airport.country = country
    airport = Repository.airports().update(airport_id, airport_name=airport_name, city=city, country=country)
    if airport is None:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    serializer = AirportSerializer(airport)
    return Response(serializer.data)

@api_view(['DELETE'])
@login_required
@user_passes_test(is_admin)
def delete_airport(request, airport_id):
    airport = Repository.airports().get_by_id(airport_id)
    if airport is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if not Repository.airports().delete(airport_id):
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@login_required
@user_passes_test(is_admin)
def get_crew_members(request):
    crew_members = Repository.crew_members().get_all()
    serializer = CrewMemberSerializer(crew_members, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@login_required
@user_passes_test(is_admin)
def get_crew_member(request, crew_member_id):
    crew_member = Repository.crew_members().get_by_id(crew_member_id)
    if crew_member is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CrewMemberSerializer(crew_member)
    return Response(serializer.data)

@api_view(['POST'])
@login_required
@user_passes_test(is_admin)
def create_crew_member(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    position = request.data.get('position')
    airplane_id = request.data.get('airplane_id')
    crew_member = Repository.crew_members().create(first_name, last_name, position, airplane_id)
    if crew_member is None:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    serializer = CrewMemberSerializer(crew_member)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@login_required
@user_passes_test(is_admin)
def update_crew_member(request, crew_member_id):
    crew_member = Repository.crew_members().get_by_id(crew_member_id)
    if crew_member is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    position = request.data.get('position')
    airplane_id = request.data.get('airplane_id')
    crew_member = Repository.crew_members().update(crew_member_id, first_name=first_name, last_name=last_name, position=position, airplane_id=airplane_id)
    if crew_member is None:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    serializer = CrewMemberSerializer(crew_member)
    return Response(serializer.data)

@api_view(['DELETE'])
@login_required
@user_passes_test(is_admin)
def delete_crew_member(request, crew_member_id):
    crew_member = Repository.crew_members().get_by_id(crew_member_id)
    if crew_member is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if not Repository.crew_members().delete(crew_member_id):
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@login_required
@user_passes_test(is_admin)
def get_flights(request):
    flights = Repository.flights().get_all()
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@login_required
@user_passes_test(is_admin)
def get_flight(request, flight_id):
    flight = Repository.flights().get_by_id(flight_id)
    if flight is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = FlightSerializer(flight)
    return Response(serializer.data)

@api_view(['POST'])
@login_required
@user_passes_test(is_admin)
def create_flight(request):
    airplane_id = request.data.get('airplane_id')
    departure_airport_id = request.data.get('departure_airport_id')
    arrival_airport_id = request.data.get('arrival_airport_id')
    departure_time = request.data.get('departure_time')
    arrival_time = request.data.get('arrival_time')
    flight = Repository.flights().create(airplane_id, departure_airport_id, arrival_airport_id, departure_time, arrival_time)
    if flight is None:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    serializer = FlightSerializer(flight)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@login_required
@user_passes_test(is_admin)
def update_flight(request, flight_id):
    flight = Repository.flights().get_by_id(flight_id)
    if flight is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    airplane_id = request.data.get('airplane_id')
    departure_airport_id = request.data.get('departure_airport_id')
    arrival_airport_id = request.data.get('arrival_airport_id')
    departure_time = request.data.get('departure_time')
    arrival_time = request.data.get('arrival_time')
    flight = Repository.flights().update(flight_id, airplane_id=airplane_id, departure_airport_id=departure_airport_id, arrival_airport_id=arrival_airport_id, departure_time=departure_time, arrival_time=arrival_time)
    if flight is None:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    serializer = FlightSerializer(flight)
    return Response(serializer.data)

@api_view(['DELETE'])
@login_required
@user_passes_test(is_admin)
def delete_flight(request, flight_id):
    flight = Repository.flights().get_by_id(flight_id)
    if flight is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if not Repository.flights().delete(flight_id):
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@login_required
@user_passes_test(is_admin)
def get_flight_reviews(request):
    flight_reviews = Repository.flight_reviews().get_all()
    serializer = FlightReviewSerializer(flight_reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@login_required
@user_passes_test(is_admin)
def get_flight_review(request, review_id):
    review = Repository.flight_reviews().get_by_id(review_id)
    if review is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = FlightReviewSerializer(review)
    return Response(serializer.data)

@api_view(['POST'])
@login_required
@user_passes_test(is_admin)
def create_flight_review(request):
    flight_id = request.data.get('flight_id')
    passenger_id = request.data.get('passenger_id')
    rating = request.data.get('rating')
    comment = request.data.get('comment')
    review_time = request.data.get('review_time')
    review = Repository.flight_reviews().create(flight_id, passenger_id, rating, comment, review_time)
    if review is None:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    serializer = FlightReviewSerializer(review)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@login_required
@user_passes_test(is_admin)
def update_flight_review(request, review_id):
    review = Repository.flight_reviews().get_by_id(review_id)
    if review is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    rating = request.data.get('rating')
    comment = request.data.get('comment')
    review = Repository.flight_reviews().update(review_id, rating=rating, comment=comment)
    if review is None:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    serializer = FlightReviewSerializer(review)
    return Response(serializer.data)

@api_view(['DELETE'])
@login_required
@user_passes_test(is_admin)
def delete_flight_review(request, review_id):
    review = Repository.flight_reviews().get_by_id(review_id)
    if review is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if not Repository.flight_reviews().delete(review_id):
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@login_required
@user_passes_test(is_admin)
def get_passengers(request):
    passengers = Repository.passengers().get_all()
    serializer = PassengerSerializer(passengers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@login_required
@user_passes_test(is_admin)
def get_passenger(request, passenger_id):
    passenger = Repository.passengers().get_by_id(passenger_id)
    if passenger is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PassengerSerializer(passenger)
    return Response(serializer.data)

@api_view(['POST'])
@login_required
@user_passes_test(is_admin)
def create_passenger(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    phone = request.data.get('phone')
    passenger = Repository.passengers().create(first_name, last_name, email, phone)
    if passenger is None:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    serializer = PassengerSerializer(passenger)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@login_required
@user_passes_test(is_admin)
def update_passenger(request, passenger_id):
    passenger = Repository.passengers().get_by_id(passenger_id)
    if passenger is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    phone = request.data.get('phone')
    passenger = Repository.passengers().update(passenger_id, first_name=first_name, last_name=last_name, email=email, phone=phone)
    if passenger is None:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    serializer = PassengerSerializer(passenger)
    return Response(serializer.data)

@api_view(['DELETE'])
@login_required
@user_passes_test(is_admin)
def delete_passenger(request, passenger_id):
    passenger = Repository.passengers().get_by_id(passenger_id)
    if passenger is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if not Repository.passengers().delete(passenger_id):
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@login_required
@user_passes_test(is_admin)
def get_bookings(request):
    bookings = Repository.bookings().get_all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@login_required
@user_passes_test(is_admin)
def get_booking(request, booking_id):
    booking = Repository.bookings().get_by_id(booking_id)
    if booking is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BookingSerializer(booking)
    return Response(serializer.data)

@api_view(['POST'])
@login_required
@user_passes_test(is_admin)
def create_booking(request):
    flight_id = request.data.get('flight_id')
    passenger_id = request.data.get('passenger_id')
    seat_number = request.data.get('seat_number')
    booking_time = request.data.get('booking_time')
    booking = Repository.bookings().create(flight_id, passenger_id, seat_number, booking_time)
    if booking is None:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    serializer = BookingSerializer(booking)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@login_required
@user_passes_test(is_admin)
def update_booking(request, booking_id):
    booking = Repository.bookings().get_by_id(booking_id)
    if booking is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    seat_number = request.data.get('seat_number')
    booking_time = request.data.get('booking_time')
    booking = Repository.bookings().update(booking_id, seat_number=seat_number, booking_time=booking_time)
    if booking is None:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    serializer = BookingSerializer(booking)
    return Response(serializer.data)

@api_view(['DELETE'])
@login_required
@user_passes_test(is_admin)
def delete_booking(request, booking_id):
    booking = Repository.bookings().get_by_id(booking_id)
    if booking is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if not Repository.bookings().delete(booking_id):
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@login_required
@user_passes_test(is_admin)
def get_passenger_insurance(request, passenger_id):
    insurance = Repository.passenger_insurance().get_by_id(passenger_id)
    if insurance is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PassengerInsuranceSerializer(insurance)
    return Response(serializer.data)

@api_view(['POST'])
@login_required
@user_passes_test(is_admin)
def create_passenger_insurance(request):
    passenger_id = request.data.get('passenger_id')
    policy_number = request.data.get('policy_number')
    coverage_amount = request.data.get('coverage_amount')
    issue_date = request.data.get('issue_date')
    expiry_date = request.data.get('expiry_date')
    insurance = Repository.passenger_insurance().create(passenger_id, policy_number, coverage_amount, issue_date, expiry_date)
    if insurance is None:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    serializer = PassengerInsuranceSerializer(insurance)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@login_required
@user_passes_test(is_admin)
def update_passenger_insurance(request, passenger_id):
    insurance = Repository.passenger_insurance().get_by_id(passenger_id)
    if insurance is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    policy_number = request.data.get('policy_number')
    coverage_amount = request.data.get('coverage_amount')
    issue_date = request.data.get('issue_date')
    expiry_date = request.data.get('expiry_date')
    insurance = Repository.passenger_insurance().update(passenger_id, policy_number=policy_number, coverage_amount=coverage_amount, issue_date=issue_date, expiry_date=expiry_date)
    if insurance is None:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    serializer = PassengerInsuranceSerializer(insurance)
    return Response(serializer.data)

@api_view(['DELETE'])
@login_required
@user_passes_test(is_admin)
def delete_passenger_insurance(request, passenger_id):
    insurance = Repository.passenger_insurance().get_by_id(passenger_id)
    if insurance is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if not Repository.passenger_insurance().delete(passenger_id):
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(status=status.HTTP_204_NO_CONTENT)
