from django import forms
from .models import (Visitor,
                     VisitorSafetyNeeds,
                     MeetingRoom, OtherRequirements)


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        exclude = ("user",)
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter position'}),
            'purpose_of_visit': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Enter purpose of visit', 'rows': 3}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter company name'}),
            'day_of_arrival': forms.DateInput(attrs={'class': 'form-control arrival_date', 'type': 'date'}),

            'day_of_departure': forms.DateInput(attrs={'class': 'form-control departure_date', 'type': 'date'}),
        }


class VisitorSafetyNeedsForm(forms.ModelForm):
    class Meta:
        model = VisitorSafetyNeeds
        exclude = ("visitor",)


class MeetingRoomForm(forms.ModelForm):
    class Meta:
        model = MeetingRoom
        exclude = ("visitor",)
        widgets = {
            'start_time': forms.DateTimeInput(format='%d/%m/%Y %H:%M:%S', attrs={'class': 'form-control start_date',
                                                                                 'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(format='%d/%m/%Y %H:%M:%S', attrs={'class': 'form-control end_date',
                                                                               'type': 'datetime-local'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'coffe': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'water': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'carbonated_drinks': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cookies': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'beamer': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'flipchart': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'stickers': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'room_others': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'others_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class OtherRequirementsForm(forms.ModelForm):
    class Meta:
        model = OtherRequirements
        exclude = ("visitor",)
