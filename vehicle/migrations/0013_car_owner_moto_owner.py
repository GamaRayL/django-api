# Generated by Django 4.2.6 on 2023-11-03 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicle', '0012_alter_mileage_moto'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='владелец'),
        ),
        migrations.AddField(
            model_name='moto',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='владелец'),
        ),
    ]
