# Generated by Django 4.0.3 on 2022-04-05 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0007_producer_publisher_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Producer',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
