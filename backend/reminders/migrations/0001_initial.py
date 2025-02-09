# Generated by Django 5.1.4 on 2025-02-02 18:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reminder_time', models.DateTimeField()),
                ('registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.registration')),
            ],
        ),
    ]
