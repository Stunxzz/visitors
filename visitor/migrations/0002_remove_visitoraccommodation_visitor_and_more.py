# Generated by Django 5.0.3 on 2024-03-30 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitoraccommodation',
            name='visitor',
        ),
        migrations.RemoveField(
            model_name='visitorsecurityinfo',
            name='visitor',
        ),
        migrations.DeleteModel(
            name='RestaurantReservation',
        ),
        migrations.DeleteModel(
            name='VisitorAccommodation',
        ),
        migrations.DeleteModel(
            name='VisitorSecurityInfo',
        ),
    ]
