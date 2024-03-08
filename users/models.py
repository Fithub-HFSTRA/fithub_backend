from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)

    Age = models.CharField(max_length=1, blank=True, null=True)

    Weight = models.CharField(max_length=1, blank=True, null=True)

    Friends_List = models.ManyToManyField('self', blank=True, symmetrical=False)

    def __str__(self):
        return self.username
    
class Heartbeat(models.Model):
    user = models.ForeignKey(CustomUser, related_name='heartbeats', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    beats_per_minute = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.timestamp} - BPM: {self.beats_per_minute}'
    
class SleepData(models.Model):
    user = models.ForeignKey(CustomUser, related_name='sleep_data', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username} - From {self.start_time} to {self.end_time}'