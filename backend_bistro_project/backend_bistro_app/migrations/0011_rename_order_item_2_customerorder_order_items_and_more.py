# Generated by Django 5.0.6 on 2024-07-16 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_bistro_app', '0010_alter_customerorder_pickup_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerorder',
            old_name='order_item_2',
            new_name='order_items',
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='pickup_time',
            field=models.TimeField(),
        ),
    ]