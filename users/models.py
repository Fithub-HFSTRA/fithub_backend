from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    BLOOD_TYPES = (
        ('AP', 'A+'),
        ('AN', 'A-'),
        ('BP', 'B+'),
        ('BN', 'B-'),
        ('ABP', 'AB+'),
        ('ABN', 'AB-'),
        ('OP', 'O+'),
        ('ON', 'O-'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)

    Age = models.CharField(max_length=1, blank=True, null=True)

    Weight = models.CharField(max_length=1, blank=True, null=True)

    first_login = models.BooleanField(blank=True,null=False,default=True)

    Friends_List = models.ManyToManyField('self', blank=True, symmetrical=False)

    pending_friend_requests = models.ManyToManyField('self', symmetrical=False, related_name='received_friend_requests', blank=True)

    first_name = models.CharField(max_length=30, blank=True)

    last_name = models.CharField(max_length=30, blank=True)

    blood_type = models.CharField(max_length=10,choices=BLOOD_TYPES,null=True, blank=True)

    wheel_chair = models.BooleanField(blank=True,null=False,default=False)

    height = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
    
class HeartbeatSummary(models.Model):
    user = models.ForeignKey(CustomUser, related_name='heartbeat_summaries', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    average_bpm = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - From {self.start_time} to {self.end_time} - Avg BPM: {self.average_bpm}'
    
class SleepData(models.Model):
    user = models.ForeignKey(CustomUser, related_name='sleepdata', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username} - From {self.start_time} to {self.end_time}'