from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task
from .serializers import TaskSerializer

class TaskGetAll(APITestCase):
    """
    Ensure we can get all tasks
    """
    def setUp(self):
        Task.objects.create(description='study python', date='2019-11-25', time='09:00:00', category='Study', priority='Medium'),
        Task.objects.create(description='read a book', date='2020-10-30', time='19:00:00', category='Study', priority='High'),
        Task.objects.create(description='play soccer', date='2019-07-21', time='21:00:00', category='Sport', priority='Medium')
    
    def test_get_all(self):
        response = self.client.get(reverse('tasks-v1'))
        print("Status GET All method = {}".format(response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 3)

class TaskPost(APITestCase):
    """
    Ensure we can create a new task
    """
    def test_post_task(self):
        url = reverse('tasks-v1')
        data = {
            'description': 'TestAPIv1',
            'date': '2020-12-31',
            'time': '10:00:00',
            'category': 'Sport',
            'priority': 'Medium'
            }
        response = self.client.post(url, data, format='json')
        print("Status POST with valid payload = {}".format(response.status_code))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().description, 'TestAPIv1')
    
    def test_invalid_post(self):
        """
        Testing a invalid payload
        """
        url = reverse('tasks-v1')
        data = {
            'description': 'Play soccer',
            'date': '2020-12-31',
            'time': '10:00:00',
            'category': 'Sport or Dinner',
            'priority': 'Medium'
            }
        response = self.client.post(url, data, format='json')
        print("Status POST with invalid payload = {}".format(response.status_code))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TaskUpdate(APITestCase):
    """
    Ensure we can update a task
    """
    def setUp(self):
        """ Create test objects in database """
        self.obj1 = Task.objects.create(description='Play Scoccer', date='2019-10-29', time='19:15:00', category='Study', priority='Medium'),
        self.obj2 = Task.objects.create(description='Study Django', date='2018-11-25', time='09:00:00', category='Study', priority='High')
        
        """ Create payloads do update objects in database """

        self.valid_data = {
            'description': 'Play Soccer',
            'date': '2019-10-29',
            'time': '19:15:00',
            'category': 'Study',
            'priority': 'Medium'
            }

        self.invalid_data = {
            'description': 'Study Django',
            'date': '2019-12-34',
            'time': '10:00:00',
            'category': 'Sporttty',
            'priority': 'Medium'
            }

    def test_put_task(self):
        """ Testing a valid payload """
        id_task = Task.objects.get(id=1).id
        url = reverse('taskdetails-v1', kwargs={'id_task': id_task})
        response = self.client.put(url, self.valid_data, format='json')
        print('Status PUT with valid payload = {}'.format(response.status_code))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.get(id=1).description, 'Play Soccer')

    def test_invalid_put(self):
        """ Testing a invalid payload """
        id_task = Task.objects.get(id=2).id
        url = reverse('taskdetails-v1', kwargs={'id_task': id_task})
        response = self.client.put(url, self.invalid_data, format='json')
        print('Status PUT with invalid payload = {}'.format(response.status_code))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TaskGetId(APITestCase):
    """
    GET task ID
    """
    def setUp(self):
        self.xyz = Task.objects.create(description='Update server', date='2019-07-15', time='00:15:00', category='Professional', priority='High')
    
    def test_ged_id(self):
        get_id = self.xyz.id
        url = reverse('taskdetails-v1', kwargs={'id_task': get_id})
        response = self.client.get(url)
        print('Status GET ID with valid id = {}'.format(response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_invalid_id(self):
        url = reverse('taskdetails-v1', kwargs={'id_task': 3568})
        response = self.client.get(url)
        print('Status GET ID with invalid id = {}'.format(response.status_code))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TaskDelete(APITestCase):
    """
    Ensure we can delete a task
    """
    def setUp(self):
        self.test_object = Task.objects.create(description='Happy hour', date='2019-07-19', time='18:15:00', category='Personal', priority='High')
    
    def test_delete_task(self):
        delete_task = self.test_object.id
        url = reverse('taskdetails-v1', kwargs={'id_task': delete_task})
        response = self.client.delete(url)
        print('Status DELETE task with valid id = {}'.format(response.status_code))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def delete_invalid_task(self):
        url = reverse('taskdetails-v1', kwargs={'id_task': 288})
        response = self.client.delete(url)
        print('Status DELETE task with invalid id = {}'.format(response.status_code))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)