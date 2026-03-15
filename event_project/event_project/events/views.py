from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, TemplateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Registration, Event
from .forms import RegistrationForm

# --- PUBLIC VIEWS ---

def home(request):
    """List all upcoming events."""
    events = Event.objects.all().order_by('date')
    return render(request, 'events/home.html', {'events': events})

class EventDetailView(DetailView):
    """View details of a single event."""
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

class RegistrationCreateView(CreateView):
    """Register for a specific event."""
    model = Registration
    form_class = RegistrationForm
    template_name = 'events/registration_form.html'
    success_url = reverse_lazy('registration_success')

    def get_initial(self):
        initial = super().get_initial()
        event_id = self.kwargs.get('event_id')
        if event_id:
            initial['event'] = get_object_or_404(Event, pk=event_id)
        return initial

    def form_valid(self, form):
        # We can add logic here to check capacity
        event = form.cleaned_data['event']
        if event.registrations.filter(status='A').count() >= event.capacity:
            messages.error(self.request, f"Sorry, {event.name} is fully booked!")
            return self.form_invalid(form)
        
        messages.success(self.request, f"Successfully registered for {event.name}!")
        return super().form_valid(form)

class SuccessView(TemplateView):
    """Simple registration success confirmation."""
    template_name = 'events/success.html'

# --- AUTH VIEWS ---

def signup(request):
    """Simple user signup."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# --- STAFF dashboard (Protected) ---

@method_decorator(staff_member_required(login_url='admin:login'), name='dispatch')
class RegistrationListView(ListView):
    """List all registrations for staff to manage."""
    model = Registration
    template_name = 'events/registration_list.html'
    context_object_name = 'registrations'

    def get_queryset(self):
        return Registration.objects.all().order_by('-created_at')

@staff_member_required(login_url='admin:login')
def update_registration_status(request, pk, action):
    """Staff only: Approve or reject a registration."""
    registration = get_object_or_404(Registration, pk=pk)

    if action == 'approve':
        registration.status = Registration.Status.APPROVED
        messages.success(request, f'Registration for {registration.name} approved.')
    elif action == 'reject':
        registration.status = Registration.Status.REJECTED
        messages.warning(request, f'Registration for {registration.name} rejected.')

    registration.save()
    return redirect('registration_list')
