# Generated by Django 5.0.2 on 2024-04-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_merge_20240402_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='blood_type',
            field=models.CharField(blank=True, choices=[('AP', 'A+'), ('AN', 'A-'), ('BP', 'B+'), ('BN', 'B-'), ('ABP', 'AB+'), ('ABN', 'AB-'), ('OP', 'O+'), ('ON', 'O-')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='height',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='wheel_chair',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_login',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
