# Generated by Django 2.2.1 on 2019-06-19 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_user_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Full_name',
            new_name='FullName',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Is_admin',
            new_name='IsAdmin',
        ),
        migrations.AlterField(
            model_name='user',
            name='CVID',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='PortfolioID',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
