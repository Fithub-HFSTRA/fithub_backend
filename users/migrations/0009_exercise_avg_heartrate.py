# Generated by Django 4.2.10 on 2024-05-02 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_exercise_fuffilment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='avg_heartrate',
            field=models.FloatField(blank=True, default=False, null=True),
        ),
    ]