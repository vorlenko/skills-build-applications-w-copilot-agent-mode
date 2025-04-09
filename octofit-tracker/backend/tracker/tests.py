from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class UserTests(APITestCase):
    def test_create_user(self):
        data = {"email": "test@example.com", "name": "Test User", "age": 25}
        response = self.client.post("/api/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@example.com", name="Test User", age=25)

    def test_create_team(self):
        data = {"name": "Test Team", "members": [str(self.user._id)]}
        response = self.client.post("/api/teams/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@example.com", name="Test User", age=25)

    def test_create_activity(self):
        data = {
            "user": str(self.user._id),
            "activity_type": "Running",
            "duration": 30,
            "date": date.today().isoformat()
        }
        response = self.client.post("/api/activities/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@example.com", name="Test User", age=25)
        self.team = Team.objects.create(name="Test Team")
        self.team.members.add(self.user)

    def test_create_leaderboard(self):
        data = {"team": str(self.team._id), "points": 100}
        response = self.client.post("/api/leaderboard/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        data = {
            "name": "Morning Yoga",
            "description": "A relaxing yoga session",
            "duration": 60
        }
        response = self.client.post("/api/workouts/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
