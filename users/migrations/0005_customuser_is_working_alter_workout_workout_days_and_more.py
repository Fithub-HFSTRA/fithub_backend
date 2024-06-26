# Generated by Django 4.2.10 on 2024-04-22 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_workout_workout_length_alter_workout_workout_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_working',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout_days',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='days that we do the workout'),
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('fuffilment', models.BooleanField(blank=True, default=False)),
                ('workout_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.workout_type')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='exercises',
            field=models.ManyToManyField(to='users.exercise'),
        ),
    ]
