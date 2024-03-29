# Generated by Django 4.1.3 on 2023-02-26 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ProductManagement', '0010_alter_product_brand_alter_product_date_last_stocked_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(choices=[('Cash', 'Cash'), ('Gcash', 'Gcash'), ('Installment', 'Installment'), ('Banking', 'Banking')], max_length=20)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('total_products', models.PositiveIntegerField()),
                ('date_of_purchace', models.DateTimeField(auto_now_add=True)),
                ('delivery_address', models.TextField(max_length=80, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('change', models.DecimalField(decimal_places=2, max_digits=5)),
                ('customer_name', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=40, null=True)),
                ('reference_no', models.CharField(max_length=40, null=True)),
                ('status', models.CharField(choices=[('complete', 'Complete'), ('pending', 'Pending')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pieces', models.PositiveIntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=9)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductManagement.product')),
                ('transaction_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_for', to='SalesTransaction.transaction')),
            ],
        ),
    ]
