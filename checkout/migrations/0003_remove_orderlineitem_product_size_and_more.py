# Generated by Django 4.2.9 on 2024-02-01 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_orderaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product_size',
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='order_line',
            field=models.IntegerField(default=10),
        ),
    ]
