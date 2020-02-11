# Generated by Django 3.0.2 on 2020-02-04 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_employee_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('sales_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=22)),
            ],
        ),
    ]