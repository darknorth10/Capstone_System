# Generated by Django 4.1.3 on 2023-04-30 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginAuthentication', '0003_customuser_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
