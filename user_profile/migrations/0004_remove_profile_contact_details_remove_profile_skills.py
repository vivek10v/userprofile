# Generated by Django 5.0.6 on 2024-05-27 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_profile_changes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='contact_details',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='skills',
        ),
    ]
