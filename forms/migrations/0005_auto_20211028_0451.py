# Generated by Django 3.0.5 on 2021-10-27 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_auto_20211027_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='Internship_Applied_for',
            new_name='Intern',
        ),
    ]
