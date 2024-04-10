from django.contrib import admin
from .models import Visitor, MeetingRoom, OutOfOfficeMeetingPlanner

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company_name', 'day_of_arrival', 'day_of_departure')
    list_filter = ('priority', 'day_of_arrival', 'day_of_departure')
    search_fields = ['first_name', 'last_name', 'company_name']
    ordering = ('-day_of_arrival',)

class MeetingRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time')
    list_filter = ('coffe', 'water', 'carbonated_drinks', 'beamer', 'flipchart')
    search_fields = ['name']
    ordering = ('name',)

class OutOfOfficeMeetingPlannerAdmin(admin.ModelAdmin):
    list_display = ('destination', 'numbers_of_people', 'transport_choice')
    list_filter = ('transport_choice',)
    search_fields = ['destination']

admin.site.register(Visitor, VisitorAdmin)
admin.site.register(MeetingRoom, MeetingRoomAdmin)
admin.site.register(OutOfOfficeMeetingPlanner, OutOfOfficeMeetingPlannerAdmin)