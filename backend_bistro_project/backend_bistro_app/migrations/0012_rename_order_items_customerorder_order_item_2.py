# Generated by Django 5.0.6 on 2024-07-16 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_bistro_app', '0011_rename_order_item_2_customerorder_order_items_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerorder',
            old_name='order_items',
            new_name='order_item_2',
        ),
    ]