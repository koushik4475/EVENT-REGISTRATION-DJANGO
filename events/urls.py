from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.RegistrationCreateView.as_view(), name='registration_create'),
    path('registrations/', views.RegistrationListView.as_view(), name='registration_list'),
    path('registration/<int:pk>/<str:action>/', views.update_registration_status, name='update_registration'),
    path('success/', views.SuccessView.as_view(), name='registration_success'),
]
