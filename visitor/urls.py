from django.urls import path
from visitor.views import MyVisitors, CreateVisitorView, UserVisitorsJsonView, \
    AddMeetingRoomToVisitorView, EditVisitorView, DeleteVisitorView

urlpatterns = (
    path('', MyVisitors.as_view(), name='visitors'),
    path('create_visitor/', CreateVisitorView.as_view(), name='create_visitor'),
    path('api_visitor/', UserVisitorsJsonView.as_view(), name='api_visitor'),
    path('add_meeting/', AddMeetingRoomToVisitorView.as_view(), name='meeting'),
    path('edit_visitor/<int:visitor_id>/', EditVisitorView.as_view(), name='edit_visitor'),
    path('delete_visitor/<int:visitor_id>/', DeleteVisitorView.as_view(), name='delete_visitor'),

)
