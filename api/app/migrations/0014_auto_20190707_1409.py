# Generated by Django 2.2 on 2019-07-07 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20190707_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='Data',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='Text',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='Title',
            field=models.TextField(null=True),
        ),
    ]
