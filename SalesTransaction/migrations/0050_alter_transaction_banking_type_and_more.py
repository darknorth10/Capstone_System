# Generated by Django 4.1.3 on 2023-04-30 03:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesTransaction', '0049_alter_transaction_installment_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='banking_type',
            field=models.CharField(blank=True, choices=[('Bank Transfer', 'Bank Transfer'), ('Cheque', 'Cheque')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='installment_due',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 30, 11, 27, 17, 549222)),
        ),
    ]
