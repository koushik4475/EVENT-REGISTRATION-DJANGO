from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, ListView, TemplateView

from .forms import RegistrationForm
from .models import Registration


def home(request):
    """Send visitors to the public registration form, never the private attendee list."""
    return redirect('registration_create')


class RegistrationCreateView(CreateView):
    model = Registration
    form_class = RegistrationForm
    template_name = 'events/registration_form.html'
    success_url = reverse_lazy('registration_success')


class SuccessView(TemplateView):
    template_name = 'events/success.html'


class RegistrationListView(ListView):
    model = Registration
    template_name = 'events/registration_list.html'
    context_object_name = 'registrations'

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Registration.objects.all().order_by('-created_at')


@staff_member_required
@require_POST
def update_registration_status(request, pk, action):
    """Allow staff to change registration status only through a POST request."""
    if action not in {'approve', 'reject'}:
        raise Http404('Unknown registration action.')

    registration = get_object_or_404(Registration, pk=pk)
    if action == 'approve':
        registration.status = Registration.Status.APPROVED
        messages.success(request, 'Registration approved successfully.')
    else:
        registration.status = Registration.Status.REJECTED
        messages.success(request, 'Registration rejected successfully.')

    registration.save(update_fields=['status'])
    return redirect('registration_list')
