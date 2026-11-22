from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Event, Registration


class RegistrationPrivacyAndStatusTests(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            name="Community Meetup",
            date=timezone.now(),
            description="A public community event.",
            capacity=25,
        )
        self.registration = Registration.objects.create(
            name="Private Registrant",
            email="registrant@example.com",
            phone="9876543210",
            event=self.event,
        )
        self.staff_user = get_user_model().objects.create_user(
            username="event-staff",
            password="test-password",
            is_staff=True,
        )

    def test_public_homepage_does_not_expose_registration_data(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Private Registrant")
        self.assertNotContains(response, "registrant@example.com")
        self.assertNotContains(response, "9876543210")

    def test_registration_list_requires_staff_access(self):
        response = self.client.get(reverse("registration_list"))

        self.assertEqual(response.status_code, 302)

    def test_status_change_rejects_get_requests(self):
        self.client.force_login(self.staff_user)
        url = reverse(
            "update_registration",
            args=[self.registration.pk, "approve"],
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, 405)
        self.registration.refresh_from_db()
        self.assertEqual(self.registration.status, Registration.Status.PENDING)

    def test_staff_can_approve_registration_with_post(self):
        self.client.force_login(self.staff_user)
        url = reverse(
            "update_registration",
            args=[self.registration.pk, "approve"],
        )

        response = self.client.post(url)

        self.assertRedirects(response, reverse("registration_list"))
        self.registration.refresh_from_db()
        self.assertEqual(self.registration.status, Registration.Status.APPROVED)

    def test_staff_cannot_use_unknown_status_action(self):
        self.client.force_login(self.staff_user)
        url = reverse(
            "update_registration",
            args=[self.registration.pk, "archive"],
        )

        response = self.client.post(url)

        self.assertEqual(response.status_code, 404)
        self.registration.refresh_from_db()
        self.assertEqual(self.registration.status, Registration.Status.PENDING)
