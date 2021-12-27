# Generated by Django 4.0 on 2021-12-27 21:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0005_server_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('f975dec0-4e0c-46fe-8b90-e69d9202b456')),
        ),
    ]