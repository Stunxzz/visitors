from django.db import models
from profiles.models import Profile
from .helper import find_max_length


class Person(models.Model):
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    position = models.CharField(max_length=105, default="")

    class Meta:
        abstract = True


class Visitor(Person):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    CHOICES_PRIORITY = [
        ("vip guest", "Vip Guest"),
        ("auditor", "Auditor"),
        ("inspection institutions", "Inspection Institutions")
    ]
    max_length_choice_priority = find_max_length(CHOICES_PRIORITY)
    purpose_of_visit = models.TextField(blank=True,null=True,max_length=1000)
    priority = models.CharField(choices=CHOICES_PRIORITY,
                                max_length=max_length_choice_priority, default='Vip Guest')
    company_name = models.CharField(max_length=50)
    day_of_arrival = models.DateField()
    day_of_departure = models.DateField()

    def __str__(self):
        return f"{self.first_name}{self.last_name}"



class MeetingRoom(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    coffe = models.BooleanField(default=False)
    water = models.BooleanField(default=False)
    carbonated_drinks = models.BooleanField(default=False)
    cookies = models.BooleanField(default=False)
    beamer = models.BooleanField(default=False)
    flipchart = models.BooleanField(default=False)
    stickers = models.BooleanField(default=False)
    room_others = models.BooleanField(default=False)
    others_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



class OutOfOfficeMeetingPlanner(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    destination = models.CharField(max_length=200, blank=True, null=True)
    CHOICES_TRANSPORT = [
        ("car", "Car"),
        ("bus", "Bus"),
        ("company_car", "Company car")
    ]
    max_length_choice_transport = find_max_length(CHOICES_TRANSPORT)
    numbers_of_people = models.IntegerField(blank=True, null=True)
    transport_choice = models.CharField(blank=True, null=True, choices=CHOICES_TRANSPORT,
                                        max_length=max_length_choice_transport)
