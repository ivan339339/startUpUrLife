# Generated by Django 2.2.1 on 2019-06-25 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190625_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='FilledSubjects',
        ),
    ]