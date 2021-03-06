# Generated by Django 4.0 on 2021-12-27 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0003_alter_serverbin_version'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('server_binary', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='servers.serverbin')),
                ('server_properties', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='servers.serverproperties')),
            ],
            options={
                'verbose_name': 'Server',
                'verbose_name_plural': 'Servers',
            },
        ),
    ]
