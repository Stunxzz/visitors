from django.urls import path
from .views import VisitorCreateView, TransportationCreateView, CombinedInfoView, CateringView, ToDoListView, \
    get_visitor_info, delete_visitor, edit_visitor, edit_visitor_transportation, edit_wab_needs, edit_last_form, \
    create_additional_visitor, delete_additional_visitor, update_additional_visitor_info

urlpatterns = [
    path('', VisitorCreateView.as_view(), name='create_visitor'),
    path("transport/<int:pk>/",TransportationCreateView.as_view(), name='transport'),
    path('combined_info/<int:pk>/', CombinedInfoView.as_view(), name='combined_info'),
    path('catering/<int:pk>/', CateringView.as_view(), name='catering_view'),
    path('visitors/', ToDoListView.as_view(), name='visitors'),
    path('visitors/get_visitor_info/<int:visitor_id>/', get_visitor_info, name='get_visitor_info'),
    path('visitors/delete_visitor/<int:visitor_id>/', delete_visitor, name='delete_visitor'),
    path('visitors/edit_visitor/<int:visitor_id>/', edit_visitor, name='edit_visitor'),
    path('visitors/edit_visitor_transportation/<int:visitor_id>/', edit_visitor_transportation,
         name='edit_visitor_transportation'),
    path('visitors/edit_wab_needs_info/<int:visitor_id>/', edit_wab_needs,
         name='edit_wab_needs'),
    path('visitors/edit_out_of_office/<int:visitor_id>/', edit_last_form,
         name='edit_last_form'),
    path('visitors/catering/<int:visitor_id>/create_additional_visitor/',create_additional_visitor,
         name='create_additional_visitor'),
    path('visitors/catering/<int:visitor_id>/update_additional_visitor_info/',update_additional_visitor_info,
         name='update_additional_visitor_info'),
    path('visitors/catering/<int:visitor_id>/delete_additional_visitor/', delete_additional_visitor,
         name='delete_additional_visitor'),
  ]