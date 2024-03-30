from django import forms
from django.forms import DateInput

from .models import (Visitor,
                     VisitorSafetyNeeds,
                     MeetingRoom, OtherRequirements)


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        exclude = ("user",)


class VisitorSafetyNeedsForm(forms.ModelForm):
    class Meta:
        model = VisitorSafetyNeeds
        exclude = ("visitor",)


class MeetingRoomForm(forms.ModelForm):
    class Meta:
        model = MeetingRoom
        exclude = ("visitor",)
        widgets = {
            'start_time': forms.DateTimeInput(format='%d/%m/%Y %H:%M:%S'),
            'end_time': forms.DateTimeInput(format='%d/%m/%Y %H:%M:%S'),
        }
        input_formats = ['%d/%m/%Y %H:%M:%S']


class OtherRequirementsForm(forms.ModelForm):
    class Meta:
        model = OtherRequirements
        exclude = ("visitor",)
