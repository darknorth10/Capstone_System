# Generated by Django 4.2 on 2023-04-09 06:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesTransaction', '0015_transaction_installment_transaction_installment_paid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='installment_due',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 14, 36, 28, 639766)),
        ),
    ]