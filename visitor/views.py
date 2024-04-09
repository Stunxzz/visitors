import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, FormView
from visitor.forms import VisitorForm,  MeetingRoomForm,  \
    OutOfOfficeMeetingPlannerForm
from visitor.models import Visitor, MeetingRoom, OutOfOfficeMeetingPlanner


class MyVisitors(LoginRequiredMixin,TemplateView):
    template_name = 'table.html'
    login_url = 'login'


class MyVisitorsMeetings(LoginRequiredMixin,TemplateView):
    template_name = 'meeting_table.html'
    login_url = 'login'


class CreateVisitorView(LoginRequiredMixin, CreateView):
    model = Visitor
    form_class = VisitorForm
    template_name = 'create_visitor.html'
    success_url = reverse_lazy('visitors')

    def form_valid(self, form):
        visitor = form.save(commit=False)
        for f in form:
            print(f.value())
        visitor.user = self.request.user
        visitor.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('more_information', kwargs={'visitor_id': self.object.id})


class UserVisitorsJsonView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        visitors = Visitor.objects.filter(user=user).values()
        visitors_data = list(visitors)

        return JsonResponse(visitors_data, safe=False)


class EditVisitorView(LoginRequiredMixin, UpdateView):
    model = Visitor
    form_class = VisitorForm
    template_name = 'edit_visitor.html'
    success_url = 'visitors'

    def get_object(self, queryset=None):
        visitor_id = self.kwargs.get('visitor_id')
        return Visitor.objects.get(pk=visitor_id)

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['visitor_id'] = self.kwargs.get('visitor_id')
        return context


class DeleteVisitorView(LoginRequiredMixin, DeleteView):
    model = Visitor
    success_url = 'visitors'

    def get_success_url(self):
        return reverse('visitors')

    def get(self, request, *args, **kwargs):
        visitor_id = self.kwargs.get('visitor_id')
        visitor = Visitor.objects.get(pk=visitor_id)
        visitor.delete()
        return HttpResponseRedirect(self.get_success_url())



class UserMeetingRoomsJsonView(View):
    def get(self, request, visitor_id, *args, **kwargs):
        user = request.user
        visitor = get_object_or_404(Visitor, pk=visitor_id, user=user)
        meeting_rooms = MeetingRoom.objects.filter(visitor=visitor)
        json_meeting_rooms = []
        for room in meeting_rooms:
            json_room = {
                'id': room.id,
                'name': room.name,
                'date': room.start_time.strftime('%d/%m/%y'),
                'start_time': room.start_time.strftime('%H:%M:%S'),
                'end_time': room.end_time.strftime('%H:%M:%S'),

            }
            json_meeting_rooms.append(json_room)

        return JsonResponse(json_meeting_rooms, safe=False)


class CalendarView(TemplateView):
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        visitor_events = []
        meeting_events = []
        for visitor in Visitor.objects.filter(user=self.request.user):
            visitor_events.append({
                'first_name': visitor.first_name,
                'last_name': visitor.last_name,
                'start': visitor.day_of_arrival.isoformat(),
                'end': visitor.day_of_departure.isoformat(),
                'priority': visitor.priority,
                'purpose_of_visit': visitor.purpose_of_visit,
                'company_name': visitor.company_name,

            })
            for meeting_room in visitor.meetingroom_set.all():
                meeting_events.append({
                    'name': meeting_room.name,
                    'start_time': meeting_room.start_time.isoformat(),
                    'end_time': meeting_room.end_time.isoformat(),

                })

        print(meeting_events)
        context['meeting_events'] = json.dumps(meeting_events)
        context['visitor_events'] = json.dumps(visitor_events)

        return context


class DeleteMeetingView(LoginRequiredMixin, DeleteView):
    model = MeetingRoom
    success_url = 'visitors'

    def get_success_url(self):
        return reverse('visitor_meetings', kwargs={'meeting_id': self.kwargs['meeting_id']})

    def get(self, request, *args, **kwargs):
        meeting_id = self.kwargs.get('meeting_id')
        meeting = MeetingRoom.objects.get(pk=meeting_id)
        meeting.delete()
        return render(request, 'calendar.html')


class MoreInformationFormView(View):
  def get(self, request, visitor_id):
    meeting_planner_form = OutOfOfficeMeetingPlannerForm()
    second_meeting = MeetingRoomForm()
    visitor = get_object_or_404(Visitor, pk=visitor_id)


    context = {

        'meeting_planner_form': meeting_planner_form,
        'second_meeting': second_meeting,
        'day_of_arrival': visitor.day_of_arrival.strftime('%Y-%m-%d'),
        'day_of_departure': visitor.day_of_departure.strftime('%Y-%m-%d')

    }
    return render(request, 'more_information.html', context)

  def post(self, request, visitor_id):
      second_meeting = MeetingRoomForm(request.POST)
      meeting_planner_form = OutOfOfficeMeetingPlannerForm(request.POST)

      if all([second_meeting.is_valid(), meeting_planner_form.is_valid(), ]):
          visitor_meeting = second_meeting.save(commit=False)
          visitor_meeting.visitor_id = visitor_id
          visitor_meeting.save()

          meeting_planner = meeting_planner_form.save(commit=False)
          meeting_planner.visitor_id = visitor_id
          meeting_planner.save()

          return redirect('visitors')
      else:

          context = {
              'visitor_meeting': second_meeting,
              'meeting_planner_form': meeting_planner_form,

          }
          return render(request, 'more_information.html', context)