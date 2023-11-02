# Generated by Django 4.2.6 on 2023-11-01 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0010_alter_mileage_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mileage',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mileage', to='vehicle.car', verbose_name='машина'),
        ),
    ]
