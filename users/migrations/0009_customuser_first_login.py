# Generated by Django 5.0.2 on 2024-04-02 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_heartbeatsummary_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='first_login',
            field=models.BooleanField(default=True),
        ),
    ]
