from django import forms
from .models import (Visitor, Transportation,
                     VisitorAccommodation, VisitorSafetyNeeds, VisitorSecurityInfo, AdditionalVisitor,
                     MeetingRoom, Catering, OutOfOfficeMeetingPlanner, RestaurantReservation, OtherRequirements)


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'



class TransportationForm(forms.ModelForm):
    class Meta:
        model = Transportation
        exclude = ("visitor",)



class VisitorAccommodationForm(forms.ModelForm):
    class Meta:
        model = VisitorAccommodation
        exclude = ("visitor",)


class VisitorSafetyNeedsForm(forms.ModelForm):
    class Meta:
        model = VisitorSafetyNeeds
        exclude = ("visitor",)


class VisitorSecurityInfoForm(forms.ModelForm):
    class Meta:
        model = VisitorSecurityInfo
        exclude = ("visitor",)


class AdditionalVisitorForm(forms.ModelForm):
    class Meta:
        model = AdditionalVisitor
        fields = '__all__'


class MeetingRoomForm(forms.ModelForm):
    class Meta:
        model = MeetingRoom
        exclude = ("visitor",)


class CateringForm(forms.ModelForm):
    class Meta:
        model = Catering
        fields = '__all__'


class OutOfOfficeMeetingPlannerForm(forms.ModelForm):
    class Meta:
        model = OutOfOfficeMeetingPlanner
        fields = '__all__'


class RestaurantReservationForm(forms.ModelForm):
    class Meta:
        model = RestaurantReservation
        fields = '__all__'


class OtherRequirementsForm(forms.ModelForm):
    class Meta:
        model = OtherRequirements
        fields = '__all__'


class CombinedForm(forms.Form):
    accommodation_form = VisitorAccommodationForm()
    safety_needs_form = VisitorSafetyNeedsForm()
    security_form = VisitorSecurityInfoForm()
    meeting_room_form = MeetingRoomForm()

    hotel_name = forms.CharField(max_length=100)
    requires_invoice = forms.BooleanField(required=False)


    reception_kpp = forms.BooleanField(required=False)
    access_card_to_kaba = forms.BooleanField(required=False)
    health_safety_training = forms.BooleanField(required=False)
    internet_accesses = forms.BooleanField(required=False)


    needs_helmet = forms.BooleanField(required=False)
    needs_vest = forms.BooleanField(required=False)
    needs_shoes = forms.BooleanField(required=False)
    size_shoes = forms.CharField(max_length=10, required=False)

    # Полета за MeetingRoom
    name = forms.CharField(max_length=100)
    start_time = forms.DateTimeField(required=False)
    end_time = forms.DateTimeField(required=False)
    coffe = forms.BooleanField(required=False)
    water = forms.BooleanField(required=False)
    carbonated_drinks = forms.BooleanField(required=False)
    cookies = forms.BooleanField(required=False)
    beamer = forms.BooleanField(required=False)
    flipchart = forms.BooleanField(required=False)
    stickers = forms.BooleanField(required=False)
    room_others = forms.BooleanField(required=False)
    others_description = forms.CharField(max_length=100, required=False)


class LastForm(forms.Form):
    catering_form = CateringForm()
    meeting_form = OutOfOfficeMeetingPlannerForm()
    restaurant = RestaurantReservationForm()
    another_visitor = AdditionalVisitorForm()
    send_menu_to_requester = forms.BooleanField(required=False)
    choose_menu_for_guest = forms.BooleanField(required=False)
    free_choice_for_company = forms.BooleanField(required=False)
    catering = forms.BooleanField(required=False)
    own_choice_menu = forms.BooleanField(required=False)
    own_free_choice = forms.BooleanField(required=False)

    CHOICES_TRANSPORT = [
        ("car", "Car"),
        ("bus", "Bus"),
        ("company_car", "Company car")
    ]

    meeting = forms.BooleanField(required=False)
    address = forms.CharField(required=False)
    destination = forms.CharField(required=False)
    numbers_of_people = forms.IntegerField(required=False)
    transport = forms.BooleanField(required=False)
    transport_choice = forms.ChoiceField(
        choices=CHOICES_TRANSPORT,
         # Този widget прави бутони за избор вместо dropdown списък
    )

    reservation = forms.BooleanField(required=False)
    restaurant_name = forms.CharField(required=False)
    number_of_people = forms.IntegerField(required=False)
    date_time = forms.DateTimeField(required=False)
    others=forms.BooleanField(required=False)
    others_thinks = forms.CharField(widget=forms.Textarea, required=False,)
    another_visitor = forms.BooleanField(required=False)
    first_name=forms.CharField(required=False)
    second_name = forms.CharField(required=False)
    company=forms.CharField(required=False)
