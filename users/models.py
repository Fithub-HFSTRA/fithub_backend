from django.contrib.auth.models import AbstractUser
from django.db import models



class Workout_Type(models.Model):
    WORKOUT_TYPES_CATS = (
        ('C', 'CARDIO'),
        ('S', 'STRENGTH'),
        ('F', 'FLEXIBILITY (INCLUDING PILATES & YOGA)'),
        ('HIIT', 'HIGH INTENSITY INTERVAL TRAINING'),
        ('W', 'WEIGHT TRAINING'),
        ('CR', 'CROSSFIT'),
    )
    name = models.CharField(max_length=30, blank=True)
    category = models.CharField(max_length=10, choices=WORKOUT_TYPES_CATS, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

class Workout(models.Model):
    workout_type = models.ForeignKey(Workout_Type, on_delete=models.CASCADE)
    #days as defined by days of the week-> each plan is done on a per-week basis and the days are 7 bit number
    #such that the days that are on(left to right) are one, and days that are off are 0
    #E.G 1000000 = 64, so a number of 64 means we only work on the first day.
    workout_days = models.PositiveIntegerField(help_text='days that we do the workout',default=0,blank=True, null=False)
    #in minutes
    workout_length = models.PositiveIntegerField(help_text='Duration of the workout in minutes', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    equipment_needed = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.workout_type.name} '
    

class Exercise(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True)
    workout_type = models.ForeignKey(Workout_Type, on_delete=models.CASCADE)
    fuffilment = models.BooleanField(blank=True, null=False, default=False)
    def __str__(self):
        return f'{self.workout_type.name} '

class Plan(models.Model):
    name = models.CharField(max_length=30, blank=True)
    creator = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    workouts = models.ManyToManyField(Workout)
    description = models.TextField(blank=True, null=True)
    difficulty_level = models.CharField(max_length=20, choices=(('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')), blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

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
    age = models.PositiveIntegerField(blank=True, null=True)
    current_workout_plan = models.OneToOneField(Plan, on_delete=models.SET_NULL, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True, help_text='Weight in kilograms')
    first_login = models.BooleanField(blank=True, null=False, default=True)
    friends_list = models.ManyToManyField('self', blank=True, symmetrical=False)
    pending_friend_requests = models.ManyToManyField('self', symmetrical=False, related_name='received_friend_requests', blank=True)
    exercises = models.ManyToManyField(Exercise)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    blood_type = models.CharField(max_length=10, choices=BLOOD_TYPES, null=True, blank=True)
    wheelchair = models.BooleanField(blank=True, null=False, default=False)
    height = models.FloatField(null=True, blank=True, help_text='Height in centimeters')
    is_working = models.BooleanField(blank=True, null=False, default=False)
    def __str__(self):
        return self.username





class SleepData(models.Model):
    user = models.ForeignKey(CustomUser, related_name='sleepdata', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username} - From {self.start_time} to {self.end_time}'

class HeartbeatSummary(models.Model):
    user = models.ForeignKey(CustomUser, related_name='heartbeat_summaries', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    average_bpm = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - From {self.start_time} to {self.end_time} - Avg BPM: {self.average_bpm}'

