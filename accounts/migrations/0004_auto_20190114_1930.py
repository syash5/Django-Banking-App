# Generated by Django 2.1 on 2019-01-14 19:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('accounts', '0003_transactions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('account_no', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(10000000), django.core.validators.MaxValueValidator(99999999)])),
                ('Interest_amount', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator('10.00')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='transactions',
            old_name='Diposit_amount',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='Interest_amount',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='Withdrawal_amount',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='account_no',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='balance',
        ),
        migrations.AddField(
            model_name='accounts',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='account_no',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='accounts.Accounts'),
            preserve_default=False,
        ),
    ]
