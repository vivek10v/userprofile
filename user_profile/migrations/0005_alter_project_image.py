# Generated by Django 5.0.6 on 2024-06-28 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_remove_profile_contact_details_remove_profile_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='project_images'),
        ),
    ]
