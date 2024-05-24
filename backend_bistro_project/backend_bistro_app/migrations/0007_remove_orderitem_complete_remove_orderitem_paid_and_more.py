# Generated by Django 5.0.6 on 2024-05-22 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_bistro_app', '0006_customerorder_order_item_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='paid',
        ),
        migrations.AddField(
            model_name='customerorder',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]