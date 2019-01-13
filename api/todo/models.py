from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Task(models.Model):
    description = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=datetime.datetime.now)
    CATEGORIES = (
        ('Personal', 'Personal'),
        ('Professional', 'Professional'),
        ('Important', 'Important'),
        ('Sport', 'Sport'),
        ('Study', 'Study'),
        ('Other', 'Other')
    )
    category = models.CharField(max_length=30, choices=CATEGORIES, default='')
    PRIORITIES = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    )
    priority =  models.CharField(max_length=10, choices=PRIORITIES, default='Low')

    def __str__(self):
        return self.description
