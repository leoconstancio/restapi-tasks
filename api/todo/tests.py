from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task

class TaskTests(APITestCase):
    def test_create_task(self):
        """
        Ensure we can create a new task
        """
        url = reverse('tasks-v1')
        data = {
            'description': 'TestAPIv1',
            'date': '2020-12-31',
            'time': '10:00:00',
            'category': 'Sport',
            'priority': 'Medium'
            }      
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().description, 'TestAPIv1')