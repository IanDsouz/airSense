# Generated by Django 4.2 on 2023-04-04 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirQualityReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
            ],
        ),
    ]
