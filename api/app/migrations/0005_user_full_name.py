# Generated by Django 2.2.1 on 2019-06-15 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_portfolio_filledsubjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Full_name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
