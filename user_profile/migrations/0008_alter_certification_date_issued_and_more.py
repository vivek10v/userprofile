# Generated by Django 5.0.6 on 2024-07-03 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_alter_education_end_date_alter_education_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='date_issued',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='end_date',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='start_date',
            field=models.CharField(max_length=200),
        ),
    ]
