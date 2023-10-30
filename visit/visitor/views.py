import json

from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, FormView, UpdateView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from datetime import datetime
from django.forms import DateTimeField
from django.http import QueryDict

from .forms import VisitorForm, TransportationForm, VisitorAccommodationForm, VisitorSecurityInfoForm, \
    VisitorSafetyNeedsForm, MeetingRoomForm, CateringForm, RestaurantReservationForm, OtherRequirementsForm, \
    AdditionalVisitorForm, CombinedForm, LastForm
from .models import Visitor, Transportation, VisitorAccommodation, VisitorSecurityInfo, VisitorSafetyNeeds, \
    MeetingRoom, Catering, OutOfOfficeMeetingPlanner, RestaurantReservation, OtherRequirements, AdditionalVisitor


def delete_additional_visitor(request, visitor_id):
    if request.method == "POST":
        data = json.loads(request.body)
        additional_visitor = get_object_or_404(AdditionalVisitor, pk=data['additional_visitor_id'])
        additional_visitor.delete()
        response_data = {'message': 'Посетителя беше изтрит успешно.'}
        return JsonResponse(response_data)
    else:
        response_data={'message': 'Грешка при изтриването!'}
        return response_data


def update_additional_visitor_info(request, visitor_id):
    if request.method == "POST":
        data = json.loads(request.body)
        additional_visitor = get_object_or_404(AdditionalVisitor, pk =data['additional_visitor_id'])
        print(additional_visitor)
        additional_visitor.first_name = data['first_name']
        additional_visitor.second_name = data['second_name']
        additional_visitor.company = data['company']
        additional_visitor.save()


        response_data = {'message': 'Информацията за посетителя беше актуализирана успешно.'}
        return JsonResponse(response_data)




def create_additional_visitor(request, visitor_id):
    if request.method == "POST":
        data = json.loads(request.body)
        first_name = data.get('first_name')
        second_name = data.get('second_name')
        company = data.get('company')
        print("?????????")

        try:
            visitor = Visitor.objects.get(id=visitor_id)
            if len(first_name)>0 and len(second_name) > 0 and len(company) > 0:
                additional_visitor = AdditionalVisitor.objects.create(
                    visitor=visitor,
                    first_name=first_name,
                    second_name=second_name,
                    company=company
            )
                additional_visitor.save()

            return JsonResponse({'message': 'Допълнителният посетител е създаден успешно'})
        except Visitor.DoesNotExist:
            return JsonResponse({'error': 'Посетителят не съществува'})
    return JsonResponse({'error': 'Методът не е поддържан'})


def edit_last_form(request, visitor_id):
    visitor = get_object_or_404(Visitor, id=visitor_id)
    catering = Catering.objects.get(visitor=visitor)
    restaurant_res = RestaurantReservation.objects.get(visitor=visitor)
    meeting = OutOfOfficeMeetingPlanner.objects.get(visitor=visitor)
    # add_visitor = AdditionalVisitor.objects.get(visitor=visitor)

    if request.method == "POST":
        form = LastForm(request.POST, initial={
            'send_menu_to_requester': catering.send_menu_to_requester,
            'choose_menu_for_guest': catering.choose_menu_for_guest,
            'free_choice_for_company': catering.free_choice_for_company,
            'catering': catering.catering,
            'own_choice_menu': catering.own_choice_menu,
            'own_free_choice': catering.own_free_choice,
            'meeting': meeting.meeting,
            'address': meeting.address,
            'destination': meeting.destination,
            'numbers_of_people': meeting.numbers_of_people,
            'transport': meeting.transport,
            'transport_choice': meeting.transport_choice,
            'reservation': restaurant_res.reservation,
            'restaurant_name': restaurant_res.restaurant_name,
            'number_of_people': restaurant_res.number_of_people,
            'date_time': restaurant_res.date_time,
            'others': restaurant_res.others,
            'others_thinks': restaurant_res.others_thinks,
            # 'another_visitor': add_visitor.another_visitor,
            # 'first_name': add_visitor.first_name,
            # 'second_name': add_visitor.second_name,
            # 'company': add_visitor.company,
        })
        if form.is_valid():
            # Обновете данните в моделите
            catering.send_menu_to_requester = form.cleaned_data['send_menu_to_requester']
            catering.choose_menu_for_guest = form.cleaned_data['choose_menu_for_guest']
            catering.free_choice_for_company = form.cleaned_data['free_choice_for_company']
            catering.catering = form.cleaned_data['catering']
            catering.own_choice_menu = form.cleaned_data['own_choice_menu']
            catering.own_free_choice = form.cleaned_data['own_free_choice']
            catering.save()

            meeting.meeting = form.cleaned_data['meeting']
            meeting.address = form.cleaned_data['address']
            meeting.destination = form.cleaned_data['destination']
            meeting.numbers_of_people = form.cleaned_data['numbers_of_people']
            meeting.transport = form.cleaned_data['transport']
            meeting.transport_choice = form.cleaned_data['transport_choice']
            meeting.save()

            restaurant_res.reservation = form.cleaned_data['reservation']
            restaurant_res.restaurant_name = form.cleaned_data['restaurant_name']
            restaurant_res.number_of_people = form.cleaned_data['number_of_people']
            restaurant_res.date_time = form.cleaned_data['date_time']
            restaurant_res.others = form.cleaned_data['others']
            restaurant_res.others_thinks = form.cleaned_data['others_thinks']
            restaurant_res.save()

            # add_visitor.another_visitor = form.cleaned_data['another_visitor']
            # add_visitor.first_name = form.cleaned_data['first_name']
            # add_visitor.second_name = form.cleaned_data['second_name']
            # add_visitor.company = form.cleaned_data['company']
            # add_visitor.save()

            return redirect('edit_visitor', visitor_id)
    else:
        form = LastForm(initial={
            'send_menu_to_requester': catering.send_menu_to_requester,
            'choose_menu_for_guest': catering.choose_menu_for_guest,
            'free_choice_for_company': catering.free_choice_for_company,
            'catering': catering.catering,
            'own_choice_menu': catering.own_choice_menu,
            'own_free_choice': catering.own_free_choice,
            'meeting': meeting.meeting,
            'address': meeting.address,
            'destination': meeting.destination,
            'numbers_of_people': meeting.numbers_of_people,
            'transport': meeting.transport,
            'transport_choice': meeting.transport_choice,
            'reservation': restaurant_res.reservation,
            'restaurant_name': restaurant_res.restaurant_name,
            'number_of_people': restaurant_res.number_of_people,
            'date_time': restaurant_res.date_time,
            'others': restaurant_res.others,
            'others_thinks': restaurant_res.others_thinks,
            # 'another_visitor': add_visitor.another_visitor,
            # 'first_name': add_visitor.first_name,
            # 'second_name': add_visitor.second_name,
            # 'company': add_visitor.company,
        })


    return render(request, 'visitor/edit_out_of_office.html', {
        'form': form,
        'visitor': visitor,
    })


def edit_wab_needs(request, visitor_id):
    visitor = get_object_or_404(Visitor, id=visitor_id)
    accommodation = VisitorAccommodation.objects.get(visitor=visitor)
    safety_needs = VisitorSafetyNeeds.objects.get(visitor=visitor)
    security_info = VisitorSecurityInfo.objects.get(visitor=visitor)
    meeting_room = MeetingRoom.objects.get(visitor=visitor)

    if request.method == "POST":
        form = CombinedForm(request.POST, initial={
            'hotel_name': accommodation.hotel_name,
            'requires_invoice': accommodation.requires_invoice,
            'reception_kpp': security_info.reception_kpp,
            'access_card_to_kaba': security_info.access_card_to_kaba,
            'health_safety_training': security_info.health_safety_training,
            'internet_accesses': security_info.internet_accesses,
            'needs_helmet': safety_needs.needs_helmet,
            'needs_vest': safety_needs.needs_vest,
            'needs_shoes': safety_needs.needs_shoes,
            'size_shoes': safety_needs.size_shoes,
            'name': meeting_room.name,
            'start_time': meeting_room.start_time,
            'end_time': meeting_room.end_time,
            'coffe': meeting_room.coffe,
            'water': meeting_room.water,
            'carbonated_drinks': meeting_room.carbonated_drinks,
            'cookies': meeting_room.cookies,
            'beamer': meeting_room.beamer,
            'flipchart': meeting_room.flipchart,
            'stickers': meeting_room.stickers,
            'room_others': meeting_room.room_others,
            'others_description': meeting_room.others_description,

        })


        if form.is_valid():
            accommodation.hotel_name = form.cleaned_data['hotel_name']
            accommodation.requires_invoice = form.cleaned_data['requires_invoice']
            accommodation.save()

            security_info.reception_kpp = form.cleaned_data['reception_kpp']
            security_info.access_card_to_kaba = form.cleaned_data['access_card_to_kaba']
            security_info.health_safety_training = form.cleaned_data['health_safety_training']
            security_info.internet_accesses = form.cleaned_data['internet_accesses']
            security_info.save()

            safety_needs.needs_helmet = form.cleaned_data['needs_helmet']
            safety_needs.needs_vest = form.cleaned_data['needs_vest']
            safety_needs.needs_shoes = form.cleaned_data['needs_shoes']
            safety_needs.size_shoes = form.cleaned_data['size_shoes']
            safety_needs.save()

            meeting_room.name = form.cleaned_data['name']
            meeting_room.start_time = form.cleaned_data['start_time']
            meeting_room.end_time = form.cleaned_data['end_time']
            meeting_room.coffe = form.cleaned_data['coffe']
            meeting_room.water = form.cleaned_data['water']
            meeting_room.carbonated_drinks = form.cleaned_data['carbonated_drinks']
            meeting_room.cookies = form.cleaned_data['cookies']
            meeting_room.beamer = form.cleaned_data['beamer']
            meeting_room.flipchart = form.cleaned_data['flipchart']
            meeting_room.stickers = form.cleaned_data['stickers']
            meeting_room.others = form.cleaned_data['room_others']
            meeting_room.others_description = form.cleaned_data['others_description']

            meeting_room.save()

            return redirect('edit_visitor', visitor_id)
    else:
        form = CombinedForm(initial={
            'hotel_name': accommodation.hotel_name,
            'requires_invoice': accommodation.requires_invoice,
            'reception_kpp': security_info.reception_kpp,
            'access_card_to_kaba': security_info.access_card_to_kaba,
            'health_safety_training': security_info.health_safety_training,
            'internet_accesses': security_info.internet_accesses,
            'needs_helmet': safety_needs.needs_helmet,
            'needs_vest': safety_needs.needs_vest,
            'needs_shoes': safety_needs.needs_shoes,
            'size_shoes': safety_needs.size_shoes,
            'name': meeting_room.name,
            'start_time': meeting_room.start_time,
            'end_time': meeting_room.end_time,
            'coffe': meeting_room.coffe,
            'water': meeting_room.water,
            'carbonated_drinks': meeting_room.carbonated_drinks,
            'cookies': meeting_room.cookies,
            'beamer': meeting_room.beamer,
            'flipchart': meeting_room.flipchart,
            'stickers': meeting_room.stickers,
            'room_others': meeting_room.room_others,
            'others_description': meeting_room.others_description,
            })


    return render(request, 'visitor/edit_wab_needs_info.html', {
        'form': form,
        'visitor_id': visitor_id,
        })


def edit_visitor(request, visitor_id):
    visitor = get_object_or_404(Visitor, id=visitor_id)

    if request.method == 'POST':
        form = VisitorForm(request.POST, instance=visitor)
        if form.is_valid():
            form.save()
        return redirect('visitors')

    else:
        form = VisitorForm(instance=visitor)

    return render(request, 'visitor/edit_visitor_info.html', {
        'form': form,
        'visitor_id': visitor_id,
    })


def edit_visitor_transportation(request, visitor_id):
    visitor = get_object_or_404(Visitor, id=visitor_id)
    try:
        transportation = Transportation.objects.get(visitor=visitor)
    except Transportation.DoesNotExist:
        transportation = None
    form = TransportationForm(request.POST, instance=transportation)
    if request.method == 'POST':
        mutable_post = request.POST.copy()
        for field_name, field in form.fields.items():
            if isinstance(field, DateTimeField):
                value = mutable_post.get(field_name)
                if value:

                    try:
                        print(value, '?????????')
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
                        print(value, "1")
                        value = value.strftime('%Y-%m-%dT%H:%M:%S')
                        print(value, '2')
                    except ValueError:

                        pass
                    mutable_post[field_name] = value
        request.POST = mutable_post
        print(request.POST)
        if form.is_valid():
            transportation = form.save(commit=False)
            transportation.visitor = visitor
            form.save()
            return redirect('edit_visitor', visitor_id)
    else:
        form = TransportationForm(instance=transportation)


    return render(request, 'visitor/edit_transportation_info.html', {
        'form': form,
        'visitor_id': visitor_id,
    })


def delete_visitor(request, visitor_id):
    print(visitor_id)
    try:
        visitor = Visitor.objects.get(id=visitor_id)
        print('deleted')
        visitor.delete()
        messages.success(request, 'Посетителят беше изтрит успешно.')
        return redirect("visitors")
    except Visitor.DoesNotExist:
        return JsonResponse({'message': 'Посетителят не беше намерен.'}, status=404)


def get_visitor_info(request, visitor_id):
    try:
        visitor = Visitor.objects.get(id=visitor_id)
        visitor_data = model_to_dict(visitor)

        transportation_data = list(visitor.transportation_set.all().values())
        accommodation_data = list(visitor.visitoraccommodation_set.all().values())
        safety_needs_data = list(visitor.visitorsafetyneeds_set.all().values())
        security_info_data = list(visitor.visitorsecurityinfo_set.all().values())
        visitor_restaurant_data = list(visitor.restaurantreservation_set.all().values())
        visitor_out_office_data = list(visitor.outofofficemeetingplanner_set.all().values())
        visitor_meeting_data = list(visitor.meetingroom_set.all().values())
        visitor_others_data = list(visitor.otherrequirements_set.all().values())
        visitor_catering_data = list(visitor.catering_set.all().values())
        visitor_additional_vis_data = list(visitor.additionalvisitor_set.all().values())
        visitor_data['transportation'] = transportation_data
        visitor_data['accommodation'] = accommodation_data
        visitor_data['safety_needs'] = safety_needs_data
        visitor_data['security_info'] = security_info_data
        visitor_data['visitor_restaurant'] = visitor_restaurant_data
        visitor_data['visitor_out_office'] = visitor_out_office_data
        visitor_data['visitor_others'] = visitor_others_data
        visitor_data['visitor_meeting'] = visitor_meeting_data
        visitor_data['visitor_catering'] = visitor_catering_data
        visitor_data['visitor_additional'] = visitor_additional_vis_data
        return JsonResponse({'visitor': visitor_data})

    except Visitor.DoesNotExist:
        return JsonResponse({'error': 'Посетителят не съществува'}, status=404)


class VisitorCreateView(CreateView):
    form_class = VisitorForm
    model = Transportation
    def get(self, request, *args, **kwargs):
        form = VisitorForm()

        context = {
            'form': form
        }
        return render(request, 'visitor/create_visitor.html', context)
    def post(self, request, *args, **kwargs):
        form = VisitorForm(request.POST)
        print(form)

        if form.is_valid():
            visitor = Visitor.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                purpose_of_visit=form.cleaned_data['purpose_of_visit'],
                company_name=form.cleaned_data['company_name'],
                position=form.cleaned_data['position'],
                priority=form.cleaned_data['priority']
            )

            visitor.save()

            return redirect(reverse('transport', kwargs={'pk': visitor.pk}))
        else:
            context = {
                'form': form
            }
            return render(request, 'visitor/create_visitor.html', context)


class TransportationCreateView(CreateView):
    form_class = TransportationForm
    template_name = 'visitor/create_transportation.html'
    success_url = reverse_lazy("combined_info")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["visitor"] = Visitor.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        visitor = Visitor.objects.get(pk=self.kwargs['pk'])
        if form.is_valid():
            transportation = Transportation.objects.create(
                visitor=visitor,
                arrival_airport=form.cleaned_data['arrival_airport'],
                airport_to_wab=form.cleaned_data['airport_to_wab'],
                airport_to_hotel=form.cleaned_data['airport_to_hotel'],
                hotel_to_wab=form.cleaned_data['hotel_to_wab'],
                own_transport=form.cleaned_data['own_transport'],
                parking=form.cleaned_data['parking'],
                parking_choice=form.cleaned_data['parking_choice'],
                wab_to_airport=form.cleaned_data['wab_to_airport'],
                hotel_to_airport=form.cleaned_data['hotel_to_airport'],
            )
            print("---------------",transportation.hotel_to_wab)
            transportation.save()
            return redirect('combined_info', pk=visitor.pk)
        return super().form_valid(form)


class CateringView(FormView):
    template_name = 'visitor/catering.html'
    form_class = LastForm
    success_url = reverse_lazy('visitors')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['visitor'] = Visitor.objects.get(pk=self.kwargs['pk'])
        print("--------")
        return context

    def form_invalid(self, form):
        print("Form is not valid!")
        for field, errors in form.errors.items():
            print(f"Field: {field}")
            for error in errors:
                print(f"Error: {error}")
        return super().form_invalid(form)

    def form_valid(self, form):
        visitor = Visitor.objects.get(pk=self.kwargs['pk'])
        if form.is_valid():
            catering_obj = Catering.objects.create(
                visitor=visitor,
                send_menu_to_requester=form.cleaned_data['send_menu_to_requester'],
                choose_menu_for_guest=form.cleaned_data['choose_menu_for_guest'],
                free_choice_for_company=form.cleaned_data['free_choice_for_company'],
                catering=form.cleaned_data['catering'],
                own_choice_menu=form.cleaned_data['own_choice_menu'],
                own_free_choice=form.cleaned_data['own_free_choice'],

            )
            catering_obj.save()

            out_office_obj = OutOfOfficeMeetingPlanner.objects.create(
                visitor=visitor,
                meeting=form.cleaned_data['meeting'],
                address=form.cleaned_data['address'],
                destination=form.cleaned_data['destination'],
                transport=form.cleaned_data['transport'],
                numbers_of_people=form.cleaned_data['numbers_of_people'],
                transport_choice=form.cleaned_data['transport_choice'],

            )
            out_office_obj.save()
            restaurant_res_obj = RestaurantReservation.objects.create(
                visitor=visitor,
                reservation=form.cleaned_data['reservation'],
                restaurant_name=form.cleaned_data['restaurant_name'],
                number_of_people = form.cleaned_data['number_of_people'],
                date_time=form.cleaned_data['date_time'],
                others_thinks=form.cleaned_data['others_thinks'],
            )
            restaurant_res_obj.save()

            other_req_obj = OtherRequirements.objects.create(
                visitor=visitor,
                others=form.cleaned_data['others'],
                others_thinks=form.cleaned_data['others_thinks']
            )
            other_req_obj.save()
            messages.success(self.request, 'Посетителят беше съсдаден успешно.')

            return redirect('visitors')


class CombinedInfoView(FormView):
    template_name = 'visitor/create_accommodation.html'
    form_class = CombinedForm
    success_url = 'catering_view'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['visitor'] = Visitor.objects.get(pk=self.kwargs['pk'])
        print("----")

        return context

    def form_valid(self, form):
        visitor = Visitor.objects.get(pk=self.kwargs['pk'])
        accommodation = VisitorAccommodation.objects.create(
            visitor=visitor,
            hotel_name=form.cleaned_data['hotel_name'],
            requires_invoice=form.cleaned_data['requires_invoice']

        )
        accommodation.save()
        security_info = VisitorSecurityInfo.objects.create(
            visitor=visitor,
            reception_kpp=form.cleaned_data['reception_kpp'],
            access_card_to_kaba=form.cleaned_data['access_card_to_kaba'],
            health_safety_training=form.cleaned_data['health_safety_training'],
            internet_accesses=form.cleaned_data['internet_accesses']
        )
        security_info.save()
        safety_needs = VisitorSafetyNeeds.objects.create(
            visitor=visitor,
            needs_helmet=form.cleaned_data['needs_helmet'],
            needs_vest=form.cleaned_data['needs_vest'],
            needs_shoes = form.cleaned_data['needs_shoes'],
            size_shoes=form.cleaned_data['size_shoes']
        )
        safety_needs.save()
        meeting_room = MeetingRoom.objects.create(
            visitor=visitor,
            name=form.cleaned_data['name'],
            start_time=form.cleaned_data['start_time'],
            end_time=form.cleaned_data['end_time'],
            coffe=form.cleaned_data['coffe'],
            water=form.cleaned_data['water'],
            carbonated_drinks=form.cleaned_data['carbonated_drinks'],
            cookies=form.cleaned_data['cookies'],
            beamer=form.cleaned_data['beamer'],
            flipchart=form.cleaned_data['flipchart'],
            stickers=form.cleaned_data['stickers'],
            room_others=form.cleaned_data['room_others'],
            others_description=form.cleaned_data['others_description']

        )
        meeting_room.save()

        return redirect('catering_view',visitor.pk)


class ToDoListView(ListView):
    model = Visitor
    template_name = 'visitor/to_do_list.html'

    def get(self, request):
        visitors = Visitor.objects.all()
        context = {"visitors": visitors}
        return render(request, self.template_name, context)
