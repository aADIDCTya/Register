# Generated by Django 3.0.5 on 2021-10-27 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_auto_20211028_0451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='gender',
            new_name='City',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='location',
            new_name='Gender',
        ),
    ]
