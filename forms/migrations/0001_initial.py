# Generated by Django 3.0.5 on 2021-10-26 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Name', models.CharField(max_length=100)),
                ('College_Name', models.TextField(blank=True)),
                ('Specialization', models.CharField(max_length=100)),
                ('Degree_Name', models.CharField(max_length=100)),
                ('Internship_Applied_For', models.CharField(max_length=100)),
                ('Phone_Number', models.CharField(max_length=100)),
                ('Email_id', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('Notes', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('datecompleted', models.DateTimeField(blank=True, null=True)),
                ('important', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]