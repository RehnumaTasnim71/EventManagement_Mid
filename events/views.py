from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse, reverse_lazy
from .models import Event
from .forms import EventForm

class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    ordering = ['date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_organizer'] = self.request.user.groups.filter(name='Organizer').exists()
        return context

class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_object()
        user = self.request.user

        context['rsvped'] = event.participants.filter(id=user.id).exists()
        context['is_participant'] = user.groups.filter(name='Participant').exists()
        context['is_organizer'] = user.groups.filter(name='Organizer').exists()
        return context

class EventCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event_list')

    def form_valid(self, form):
        form.instance.organizer = self.request.user  
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.groups.filter(name='Organizer').exists()

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'

    def test_func(self):
        return self.request.user.groups.filter(name='Organizer').exists()
    
    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('event_detail', args=[self.object.id])

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('event_list')

    def test_func(self):
        return self.request.user.groups.filter(name='Organizer').exists()

class RSVPEventView(LoginRequiredMixin, View):
    def post(self, request, event_id, *args, **kwargs):
        event = get_object_or_404(Event, id=event_id)

        if event.participants.filter(id=request.user.id).exists():
            messages.info(request, "You already RSVP'd to this event.")
        else:
            event.participants.add(request.user)
            messages.success(request, 'RSVP confirmed! A confirmation email was sent.')

        return redirect(reverse('event_detail', args=[event.id]))

class DashboardView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "events/dashboard.html"
    context_object_name = "events"

    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user)

class HomeRedirectView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Redirect logged-in users to event list (dashboard)
            return redirect('event_list')
        else:
            # Redirect anonymous users to login page
            return redirect('login')

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/create.html'
    success_url = reverse_lazy('event_list') 