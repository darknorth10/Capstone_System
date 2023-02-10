# Generated by Django 4.1.3 on 2023-02-10 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginAuthentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('cashier', 'Cashier'), ('admin', 'Admin')], default='Cashier', max_length=7),
        ),
    ]
