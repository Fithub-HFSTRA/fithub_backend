# Generated by Django 4.2.10 on 2024-04-02 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_workout_time_workout_workout_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='workout_length',
            field=models.PositiveIntegerField(blank=True, help_text='Duration of the workout in minutes', null=True),
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout_days',
            field=models.PositiveIntegerField(blank=True, help_text='days that we do the workout', null=True),
        ),
    ]