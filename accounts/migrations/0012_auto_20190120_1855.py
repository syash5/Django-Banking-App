# Generated by Django 2.1 on 2019-01-20 18:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('accounts', '0011_auto_20190119_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='account_no',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='account_no',
            field=models.PositiveIntegerField(default=1, unique=True, validators=[django.core.validators.MinValueValidator(10000000), django.core.validators.MaxValueValidator(99999999)]),
        ),
    ]
