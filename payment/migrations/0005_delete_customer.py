# Generated by Django 3.1 on 2021-11-08 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20211104_1117'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]