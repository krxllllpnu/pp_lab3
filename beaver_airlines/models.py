# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)

    def __str__(self):
        return self.username

class Airplane(models.Model):
    airplane_id = models.AutoField(primary_key=True)
    manufacturer = models.CharField(max_length=15, blank=True, null=True)
    model = models.CharField(max_length=15, blank=True, null=True)
    capacity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'airplane'


class Airport(models.Model):
    airport_id = models.AutoField(primary_key=True)
    airport_name = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=25)
    country = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'airport'


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    flight = models.ForeignKey('Flight', models.DO_NOTHING)
    passenger = models.ForeignKey('Passenger', models.DO_NOTHING)
    seat_number = models.CharField(max_length=6)
    booking_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'booking'


class CrewMember(models.Model):
    crew_member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50, blank=True, null=True)
    airplane = models.ForeignKey(Airplane, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crew_member'


class Flight(models.Model):
    flight_id = models.AutoField(primary_key=True)
    airplane = models.ForeignKey(Airplane, models.DO_NOTHING)
    departure_airport = models.ForeignKey(Airport, models.DO_NOTHING)
    arrival_airport = models.ForeignKey(Airport, models.DO_NOTHING, related_name='flight_arrival_airport_set')
    departure_time = models.DateTimeField(blank=True, null=True)
    arrival_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flight'


class FlightReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    flight = models.ForeignKey(Flight, models.DO_NOTHING)
    passenger = models.ForeignKey('Passenger', models.DO_NOTHING)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    review_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'flight_review'


class Passenger(models.Model):
    passenger_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'passenger'


class PassengerInsurance(models.Model):
    passenger = models.OneToOneField(Passenger, models.DO_NOTHING, primary_key=True)
    policy_number = models.CharField(max_length=50)
    coverage_amount = models.DecimalField(max_digits=10, decimal_places=2)
    issue_date = models.DateField()
    expiry_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'passenger_insurance'
