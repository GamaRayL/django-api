# Generated by Django 4.2.6 on 2023-10-27 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_rename_card_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'мотоцикл',
                'verbose_name_plural': 'мотоциклы',
            },
        ),
    ]
