# Generated by Django 2.2 on 2019-06-23 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20190623_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='BirthDate',
            field=models.DateField(null=True),
        ),
    ]