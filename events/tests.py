from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Event, Registration


class RegistrationPrivacyAndStatusTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.event = Event.objects.create(
            name='Community Meetup',
            date='2030-05-01T10:00:00Z',
            description='A test event',
            capacity=25,
        )
        cls.registration = Registration.objects.create(
            name='Private Attendee',
            email='attendee@example.com',
            phone='1234567890',
            event=cls.event,
        )

    def test_home_redirects_to_public_registration_form(self):
        response = self.client.get(reverse('home'))

        self.assertRedirects(response, reverse('registration_create'))
        self.assertNotContains(response, 'Private Attendee')

    def test_registration_list_requires_staff(self):
        response = self.client.get(reverse('registration_list'))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_status_change_rejects_get_requests(self):
        user = get_user_model().objects.create_user(
            username='staff', password='test-password', is_staff=True
        )
        self.client.force_login(user)

        response = self.client.get(
            reverse('update_registration', args=[self.registration.pk, 'approve'])
        )

        self.assertEqual(response.status_code, 405)
        self.registration.refresh_from_db()
        self.assertEqual(self.registration.status, Registration.Status.PENDING)

    def test_staff_can_update_status_with_post(self):
        user = get_user_model().objects.create_user(
            username='staff', password='test-password', is_staff=True
        )
        self.client.force_login(user)

        response = self.client.post(
            reverse('update_registration', args=[self.registration.pk, 'approve'])
        )

        self.assertRedirects(response, reverse('registration_list'))
        self.registration.refresh_from_db()
        self.assertEqual(self.registration.status, Registration.Status.APPROVED)

    def test_non_staff_cannot_update_status(self):
        user = get_user_model().objects.create_user(
            username='member', password='test-password'
        )
        self.client.force_login(user)

        response = self.client.post(
            reverse('update_registration', args=[self.registration.pk, 'reject'])
        )

        self.assertEqual(response.status_code, 302)
        self.registration.refresh_from_db()
        self.assertEqual(self.registration.status, Registration.Status.PENDING)

    def test_unknown_status_action_returns_404(self):
        user = get_user_model().objects.create_user(
            username='staff', password='test-password', is_staff=True
        )
        self.client.force_login(user)

        response = self.client.post(
            reverse('update_registration', args=[self.registration.pk, 'delete'])
        )

        self.assertEqual(response.status_code, 404)
