from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .models import Registration, Event
from .forms import RegistrationForm


# ✅ Home view → show registration list instead of missing home.html
def home(request):
    registrations = Registration.objects.all().order_by('-created_at')
    return render(request, 'events/registration_list.html', {'registrations': registrations})


# ✅ Registration form (create view)
class RegistrationCreateView(CreateView):
    model = Registration
    form_class = RegistrationForm
    template_name = 'events/registration_form.html'
    success_url = reverse_lazy('registration_success')


# ✅ Success page after registration
class SuccessView(TemplateView):
    template_name = 'events/success.html'


# ✅ Registration list (staff only)
class RegistrationListView(ListView):
    model = Registration
    template_name = 'events/registration_list.html'
    context_object_name = 'registrations'

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Registration.objects.all().order_by('-created_at')


# ✅ Update registration status (approve/reject) → staff only
@staff_member_required
def update_registration_status(request, pk, action):
    registration = get_object_or_404(Registration, pk=pk)

    if action == 'approve':
        registration.status = Registration.Status.APPROVED
        messages.success(request, 'Registration approved successfully.')
    elif action == 'reject':
        registration.status = Registration.Status.REJECTED
        messages.success(request, 'Registration rejected successfully.')

    registration.save()
    return redirect('registration_list')
