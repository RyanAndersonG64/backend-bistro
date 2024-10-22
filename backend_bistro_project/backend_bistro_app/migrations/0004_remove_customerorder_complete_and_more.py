# Generated by Django 5.0.6 on 2024-05-22 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_bistro_app', '0003_allergen_remove_menuitem_allergens_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerorder',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='customerorder',
            name='paid',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='paid',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='pickup_time',
            field=models.TimeField(),
        ),
    ]
