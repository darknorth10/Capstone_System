# Generated by Django 4.2 on 2023-04-11 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerProfile', '0003_alter_customer_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='credit_eligibility',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20),
        ),
    ]