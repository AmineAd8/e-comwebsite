# Generated by Django 4.2.8 on 2025-02-18 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_ordermodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitemmodel',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
