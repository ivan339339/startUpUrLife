# Generated by Django 2.2 on 2019-06-23 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190620_1440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Adress',
            new_name='Address',
        ),
    ]
