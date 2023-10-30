

from django.db import models
from .helper import find_max_length


class Person(models.Model):
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    position = models.CharField(max_length=105, default="")

    class Meta:
        abstract = True


# class Host(Person):
#
#     def __str__(self):
#         return f"{self.first_name}{self.last_name}"
#

class Visitor(Person):
    CHOICES_PRIORITY = [
        ("vip guest", "Vip Guest"),
        ("auditor", "Auditor"),
        ("inspection institutions", "Inspection Institutions")
    ]
    max_length_choice_priority = find_max_length(CHOICES_PRIORITY)
    #host = models.ForeignKey(Host, on_delete=models.CASCADE,blank=True,null=True)
    purpose_of_visit = models.TextField(blank=True,null=True,max_length=1000)
    priority = models.CharField(choices=CHOICES_PRIORITY,
                                max_length=max_length_choice_priority, default='Vip Guest')
    company_name = models.CharField(max_length=50)
    # day_of_arrival = models.DateField(
    #     blank=False, null=False,
    #     default="",
    # )
    # day_of_departure = models.DateField(
    #     blank=False, null=False,
    #     default="",
    # )

    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class Transportation(models.Model):
    # Изборът е винаги лист от tuple винаги има 2 стойности 1стойноста се запазва в базата данни 2това което ще се визуализира на екрана
    CHOICES_PARKING = [
        ("outside", "Outside"),
        ("inside", "Inside")
    ]
    max_length_choice_parking = find_max_length(CHOICES_PARKING)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    arrival_airport = models.DateTimeField(blank=True, null=True)
    airport_to_wab = models.DateTimeField(blank=True, null=True)
    airport_to_hotel = models.DateTimeField(blank=True, null=True)
    hotel_to_wab = models.DateTimeField(blank=True, null=True)
    wab_to_hotel = models.DateTimeField(blank=True, null=True)
    own_transport = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    parking_choice = models.CharField(blank=True, null=True, choices=CHOICES_PARKING,
                                      max_length=max_length_choice_parking)
    wab_to_airport = models.DateTimeField(blank=True, null=True)
    hotel_to_airport = models.DateTimeField(blank=True, null=True)

    # TODO трябва да се направи меню за избор на вътрешен или външен паркинг


class VisitorAccommodation(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=100,blank=True,null=True)
    requires_invoice = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.visitor}'s Accommodation at {self.hotel_name}"


class VisitorSecurityInfo(models.Model):
    visitor = models.ForeignKey(Visitor,on_delete=models.CASCADE)
    reception_kpp = models.BooleanField(default=False)
    access_card_to_kaba = models.BooleanField(default=False)
    health_safety_training = models.BooleanField(default=False)
    internet_accesses = models.BooleanField(default=False)


class VisitorSafetyNeeds(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    needs_helmet = models.BooleanField(default=False)
    needs_vest = models.BooleanField(default=False)
    needs_shoes = models.BooleanField(default=False)
    size_shoes = models.CharField(max_length=5,null=True, blank=True)

    def __str__(self):
        return f"Safety Needs for {self.visitor}"


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
    # TODO за others трябва да се направи падащо меню
    others_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Catering(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    send_menu_to_requester = models.BooleanField(default=False)
    choose_menu_for_guest = models.BooleanField(default=False)
    free_choice_for_company = models.BooleanField(default=False)
    catering = models.BooleanField(default=False)
    # TODO за собствена сметка на поситителя
    own_choice_menu = models.BooleanField(default=False)
    own_free_choice = models.BooleanField(default=False)


class OutOfOfficeMeetingPlanner(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    meeting = models.BooleanField(default=False)
    # TODO при среща трябва да се добави адрес и дестинация
    address = models.CharField(max_length=200, blank=True, null=True)
    destination = models.CharField(max_length=200, blank=True, null=True)
    CHOICES_TRANSPORT = [
        ("car", "Car"),
        ("bus", "Bus"),
        ("company_car", "Company car")
    ]
    transport = models.BooleanField(default=False)
    max_length_choice_transport = find_max_length(CHOICES_TRANSPORT)
    # TODO при танспорт трябва да има бр.хора и какъв транспорт ще е необходимо
    numbers_of_people = models.IntegerField(blank=True, null=True)
    transport_choice = models.CharField(blank=True, null=True, choices=CHOICES_TRANSPORT,
                                        max_length=max_length_choice_transport)


class RestaurantReservation(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    reservation = models.BooleanField(default=False)
    # TODO име,брой хора, [час]
    # да потърся поле за час и дата
    restaurant_name = models.CharField(blank=True, null=True, max_length=200)
    number_of_people = models.IntegerField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True,null=True)
    others = models.BooleanField(default=False)
    others_thinks = models.TextField(blank=True, null=True)


class OtherRequirements(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    others = models.BooleanField(default=False)
    # TODO добавяне на текс ареа
    others_thinks = models.TextField(max_length=200, blank=True, null=True)


class AdditionalVisitor(models.Model):

    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    another_visitor = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    second_name = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return f"{self.first_name} -  {self.second_name} - {self.company}"



