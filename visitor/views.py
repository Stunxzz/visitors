from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from visitor.forms import VisitorForm, VisitorSafetyNeedsForm, MeetingRoomForm, OtherRequirementsForm
from visitor.models import Visitor, MeetingRoom


class MyVisitors(LoginRequiredMixin,TemplateView):
    template_name = 'table.html'
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


class UserVisitorsJsonView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        visitors = Visitor.objects.filter(user=user).values()
        visitors_data = list(visitors)

        return JsonResponse(visitors_data, safe=False)


class AddMeetingRoomToVisitorView(LoginRequiredMixin, CreateView):
    model = MeetingRoom
    form_class = MeetingRoomForm
    template_name = 'add_meeting_room.html'

    def form_valid(self, form):
        current_user = self.request.user
        last_visitor = Visitor.objects.filter(user=current_user).last()
        print(last_visitor.id)
        form.instance.visitor_id = last_visitor.id
        return super().form_valid(form)


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