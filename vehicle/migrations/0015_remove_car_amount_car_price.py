# Generated by Django 4.2.7 on 2023-11-14 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0014_car_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='amount',
        ),
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]