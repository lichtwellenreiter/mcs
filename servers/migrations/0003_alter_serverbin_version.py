# Generated by Django 4.0 on 2021-12-27 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0002_serverbin_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverbin',
            name='version',
            field=models.CharField(max_length=10),
        ),
    ]
