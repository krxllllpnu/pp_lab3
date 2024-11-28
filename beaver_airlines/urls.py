from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('bookings/add/', views.booking_form, name='booking_add_by_user'),
    path('api/flights/available/<int:departure_airport_id>/<int:arrival_airport_id>/', views.get_available_flights, name='get_available_flights'),
    path('passengers/add/', views.add_passenger_by_user, name='add_passenger_by_user'),
    path('insurance/add/<int:passenger_id>/', views.add_insurance_by_user, name='add_insurance_by_user'),
    path('bookings/edit/<int:booking_id>/', views.booking_edit_by_user, name='booking_edit_by_user'),
    path('bookings/delete/<int:booking_id>/', views.delete_booking_by_user, name='delete_booking_by_user'),
    path('bookings/<int:booking_id>/confirm_delete/', views.confirm_delete_booking, name='confirm_delete_booking'),
    path('api/reports/average_rating_per_flight/', views.get_average_rating_per_flight, name='get_average_rating_per_flight'),
    path('api/reports/top_passengers/', views.get_passengers_with_most_bookings, name='get_passengers_with_most_bookings'),
    path('api/reports/flight_durations/', views.get_flight_durations, name='get_flight_durations'),
    path('api/reports/average_flight_duration/', views.get_average_flight_duration, name='get_average_flight_duration'),
    path('api/reports/top_flights/', views.get_flights_with_most_bookings, name='get_flights_with_most_bookings'),
    path('api/reports/top_airplanes/', views.get_airplanes_with_most_flights, name='get_airplanes_with_most_flights'),
    path('api/reports/top_airports/', views.get_airports_with_most_departures, name='get_airports_with_most_departures'),
    path('api/reports/top_crew_members/', views.get_crew_members_with_most_airplanes, name='get_crew_members_with_most_airplanes'),
    path('api/airplanes/', views.get_airplanes, name='get_airplanes'),
    path('api/airplanes/<int:airplane_id>/', views.get_airplane, name='get_airplane'),
    path('api/airplanes/create', views.create_airplane, name='create_airplane'),
    path('api/airplanes/update/<int:airplane_id>/', views.update_airplane, name='update_airplane'),
    path('api/airplanes/delete/<int:airplane_id>/', views.delete_airplane, name='delete_airplane'),
    path('api/airports/', views.get_airports, name='get_airports'),
    path('api/airports/<int:airport_id>/', views.get_airport, name='get_airport'),
    path('api/airports/create', views.create_airport, name='create_airport'),
    path('api/airports/update/<int:airport_id>/', views.update_airport, name='update_airport'),
    path('api/airports/delete/<int:airport_id>/', views.delete_airport, name='delete_airport'),
    path('api/crew_members/', views.get_crew_members, name='get_crew_members'),
    path('api/crew_members/<int:crew_member_id>/', views.get_crew_member, name='get_crew_member'),
    path('api/crew_members/create', views.create_crew_member, name='create_crew_member'),
    path('api/crew_members/update/<int:crew_member_id>/', views.update_crew_member, name='update_crew_member'),
    path('api/crew_members/delete/<int:crew_member_id>/', views.delete_crew_member, name='delete_crew_member'),
    path('api/flights/', views.get_flights, name='get_flights'),
    path('api/flights/<int:flight_id>/', views.get_flight, name='get_flight'),
    path('api/flights/create', views.create_flight, name='create_flight'),
    path('api/flights/update/<int:flight_id>/', views.update_flight, name='update_flight'),
    path('api/flights/delete/<int:flight_id>/', views.delete_flight, name='delete_flight'),
    path('api/passengers/', views.get_passengers, name='get_passengers'),
    path('api/passengers/<int:passenger_id>/', views.get_passenger, name='get_passenger'),
    path('api/passengers/create', views.create_passenger, name='create_passenger'),
    path('api/passengers/update/<int:passenger_id>/', views.update_passenger, name='update_passenger'),
    path('api/passengers/delete/<int:passenger_id>/', views.delete_passenger, name='delete_passenger'),
    path('api/passenger_insurances/<int:passenger_id>/', views.get_passenger_insurance, name='get_passenger_insurance'),
    path('api/passenger_insurances/create', views.create_passenger_insurance, name='create_passenger_insurance'),
    path('api/passenger_insurances/update/<int:passenger_id>/', views.update_passenger_insurance, name='update_passenger_insurance'),
    path('api/passenger_insurances/delete/<int:passenger_id>/', views.delete_passenger_insurance, name='delete_passenger_insurance'),
    path('api/bookings/', views.get_bookings, name='get_bookings'),
    path('api/bookings/<int:booking_id>/', views.get_booking, name='get_booking'),
    path('api/bookings/create', views.create_booking, name='create_booking'),
    path('api/bookings/update/<int:booking_id>/', views.update_booking, name='update_booking'),
    path('api/bookings/delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('api/flight_reviews/', views.get_flight_reviews, name='get_flight_reviews'),
    path('api/flight_reviews/<int:flight_review_id>/', views.get_flight_review, name='get_flight_review'),
    path('api/flight_reviews/create', views.create_flight_review, name='create_flight_review'),
    path('api/flight_reviews/update/<int:flight_review_id>/', views.update_flight_review, name='update_flight_review'),
    path('api/flight_reviews/delete/<int:flight_review_id>/', views.delete_flight_review, name='delete_flight_review'),
]
