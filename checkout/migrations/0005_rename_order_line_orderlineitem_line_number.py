# Generated by Django 4.2.9 on 2024-02-01 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_remove_orderlineitem_quantity_orderlineitem_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='order_line',
            new_name='line_number',
        ),
    ]
