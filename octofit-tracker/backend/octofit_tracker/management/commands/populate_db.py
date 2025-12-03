from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create Users (superheroes)
        users = [
            User(email='tony@marvel.com', name='Tony Stark', team='marvel', is_superhero=True),
            User(email='steve@marvel.com', name='Steve Rogers', team='marvel', is_superhero=True),
            User(email='bruce@marvel.com', name='Bruce Banner', team='marvel', is_superhero=True),
            User(email='clark@dc.com', name='Clark Kent', team='dc', is_superhero=True),
            User(email='bruce@dc.com', name='Bruce Wayne', team='dc', is_superhero=True),
            User(email='diana@dc.com', name='Diana Prince', team='dc', is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Create Activities
        tony = User.objects.get(email='tony@marvel.com')
        clark = User.objects.get(email='clark@dc.com')
        Activity.objects.create(user=tony, activity_type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=clark, activity_type='swim', duration=45, date=timezone.now().date())

        # Create Workouts
        Workout.objects.create(name='Pushups', description='Upper body strength', suggested_for='marvel')
        Workout.objects.create(name='Flight', description='Aerobic endurance', suggested_for='dc')

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=200)
        Leaderboard.objects.create(team=dc, points=180)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
