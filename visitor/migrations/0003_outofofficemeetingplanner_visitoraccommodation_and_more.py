# Generated by Django 4.2.11 on 2024-04-09 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0002_remove_visitoraccommodation_visitor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutOfOfficeMeetingPlanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(blank=True, max_length=200, null=True)),
                ('transport', models.BooleanField(default=False)),
                ('numbers_of_people', models.IntegerField(blank=True, null=True)),
                ('transport_choice', models.CharField(blank=True, choices=[('car', 'Car'), ('bus', 'Bus'), ('company_car', 'Company car')], max_length=11, null=True)),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor.visitor')),
            ],
        ),
        migrations.CreateModel(
            name='VisitorAccommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(blank=True, max_length=100, null=True)),
                ('requires_invoice', models.BooleanField(default=False)),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor.visitor')),
            ],
        ),
        migrations.DeleteModel(
            name='OtherRequirements',
        ),
    ]
