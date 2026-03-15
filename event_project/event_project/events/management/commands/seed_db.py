import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from events.models import Event
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Seeds the database with initial demo data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database...')

        # Create Admin
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin')
            self.stdout.write(self.style.SUCCESS('Admin created (admin/admin)'))

        # Create Test User
        if not User.objects.filter(username='user').exists():
            User.objects.create_user('user', 'user@example.com', 'user')
            self.stdout.write(self.style.SUCCESS('User created (user/user)'))

        # Create Demo Events
        events_data = [
            {
                'name': 'AI & Future Tech Summit 2026',
                'description': 'A premium gathering of world-class AI researchers and tech industry leaders discussing the next decade of innovation.',
                'capacity': 500,
                'days_forward': 30
            },
            {
                'name': 'Luxury Web Design Workshop',
                'description': 'Master the art of creating high-end, cinematic web experiences using modern frameworks and 3D technologies.',
                'capacity': 50,
                'days_forward': 15
            },
            {
                'name': 'Global Innovation Gala',
                'description': 'Celebrate the finest achievements in technology and design at this ultra-exclusive black-tie event.',
                'capacity': 200,
                'days_forward': 60
            }
        ]

        for data in events_data:
            if not Event.objects.filter(name=data['name']).exists():
                Event.objects.create(
                    name=data['name'],
                    description=data['description'],
                    capacity=data['capacity'],
                    date=timezone.now() + timedelta(days=data['days_forward'])
                )
                self.stdout.write(self.style.SUCCESS(f"Event '{data['name']}' created."))

        self.stdout.write(self.style.SUCCESS('Database seeding complete!'))
