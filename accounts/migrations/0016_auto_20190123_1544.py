# Generated by Django 2.1 on 2019-01-23 15:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_userprofile_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='account_no',
            field=models.PositiveIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(10000000), django.core.validators.MaxValueValidator(99999999)]),
        ),
    ]