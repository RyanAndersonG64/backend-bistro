# Generated by Django 5.0.6 on 2024-07-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_bistro_app', '0013_rename_order_item_2_customerorder_order_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='dine_in',
            field=models.BooleanField(),
        ),
    ]
