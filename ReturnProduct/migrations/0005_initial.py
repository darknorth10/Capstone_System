# Generated by Django 4.1.3 on 2023-04-26 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ReturnProduct', '0004_delete_productarchive'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('size', models.CharField(max_length=40)),
                ('quantity', models.IntegerField()),
                ('transact_no', models.IntegerField()),
            ],
        ),
    ]
