from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('events/<int:event_id>/register/', views.RegistrationCreateView.as_view(), name='registration_create_specific'),
    path('register/', views.RegistrationCreateView.as_view(), name='registration_create'),
    path('success/', views.SuccessView.as_view(), name='registration_success'),
    path('dashboard/', views.RegistrationListView.as_view(), name='registration_list'),
    path('registration/<int:pk>/<str:action>/', views.update_registration_status, name='update_registration_status'),
]
