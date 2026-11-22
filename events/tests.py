from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Event, Registration


class RegistrationAccessTests(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            name="Community meetup",
            date="2030-01-01T10:00:00Z",
            description="A public event",
            capacity=20,
        )
        self.registration = Registration.objects.create(
            name="Private attendee",
            email="attendee@example.com",
            phone="1234567890",
            event=self.event,
        )
        self.staff = get_user_model().objects.create_user(
            username="staff",
            password="test-password",
            is_staff=True,
        )

    def test_home_redirects_to_public_registration_form(self):
        response = self.client.get(reverse("home"))

        self.assertRedirects(response, reverse("registration_create"))
        self.assertNotContains(response, "Private attendee")

    def test_registration_list_requires_staff(self):
        response = self.client.get(reverse("registration_list"))

        self.assertEqual(response.status_code, 302)
        self.assertIn("/admin/login/", response.url)

    def test_staff_cannot_change_status_with_get(self):
        self.client.force_login(self.staff)

        response = self.client.get(
            reverse(
                "update_registration",
                args=[self.registration.pk, "approve"],
            )
        )

        self.assertEqual(response.status_code, 405)
        self.registration.refresh_from_db()
        self.assertEqual(self.registration.status, Registration.Status.PENDING)

    def test_staff_can_approve_with_post(self):
        self.client.force_login(self.staff)

        response = self.client.post(
            reverse(
                "update_registration",
                args=[self.registration.pk, "approve"],
            )
        )

        self.assertRedirects(response, reverse("registration_list"))
        self.registration.refresh_from_db()
        self.assertEqual(self.registration.status, Registration.Status.APPROVED)

    def test_unknown_action_returns_404_without_changing_status(self):
        self.client.force_login(self.staff)

        response = self.client.post(
            reverse(
                "update_registration",
                args=[self.registration.pk, "archive"],
            )
        )

        self.assertEqual(response.status_code, 404)
        self.registration.refresh_from_db()
        self.assertEqual(self.registration.status, Registration.Status.PENDING)
