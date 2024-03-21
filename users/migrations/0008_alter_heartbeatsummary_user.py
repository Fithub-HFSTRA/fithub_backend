# Generated by Django 4.2.10 on 2024-03-19 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_heartbeatsummary_alter_sleepdata_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heartbeatsummary',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heartbeat_summaries', to=settings.AUTH_USER_MODEL),
        ),
    ]