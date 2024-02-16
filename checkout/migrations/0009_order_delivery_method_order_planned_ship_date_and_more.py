# Generated by Django 4.2.9 on 2024-02-14 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_rename_original_bag_order_original_basket'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(default='REGPOST', max_length=7),
        ),
        migrations.AddField(
            model_name='order',
            name='planned_ship_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 28, 18, 16, 39, 428607, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='line_ship_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 15, 18, 16, 39, 429225, tzinfo=datetime.timezone.utc)),
        ),
    ]