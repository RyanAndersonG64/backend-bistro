# Generated by Django 5.0.6 on 2024-07-23 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_bistro_app', '0014_alter_customerorder_dine_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='dine_status',
            field=models.TextField(default=69),
            preserve_default=False,
        ),
    ]