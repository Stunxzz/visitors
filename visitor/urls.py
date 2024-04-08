from django.urls import path
from visitor.views import MyVisitors, CreateVisitorView, UserVisitorsJsonView, \
    EditVisitorView, DeleteVisitorView, CreateMeetingRoomView, UserMeetingRoomsJsonView, \
    MyVisitorsMeetings, CalendarView, DeleteMeetingView

urlpatterns = (
    path('', MyVisitors.as_view(), name='visitors'),
    path('create_visitor/', CreateVisitorView.as_view(), name='create_visitor'),
    path('api_visitor/', UserVisitorsJsonView.as_view(), name='api_visitor'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('api_meetings/<int:visitor_id>/', UserMeetingRoomsJsonView.as_view(), name='api_meetings'),
    path('edit_visitor/<int:visitor_id>/', EditVisitorView.as_view(), name='edit_visitor'),
    path('delete_meeting/<int:meeting_id>/', DeleteMeetingView.as_view(), name='delete_meeting'),
    path('visitor_meetings/<int:visitor_id>/', MyVisitorsMeetings.as_view(), name='visitor_meetings'),
    path('delete_visitor/<int:visitor_id>/', DeleteVisitorView.as_view(), name='delete_visitor'),
    path('create_meeting/<int:visitor_id>/', CreateMeetingRoomView.as_view(), name='create_meeting'),

)
