# Generated by Django 5.0.6 on 2024-05-22 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_bistro_app', '0004_remove_customerorder_complete_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
