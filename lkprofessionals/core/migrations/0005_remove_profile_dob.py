# Generated by Django 5.1 on 2024-08-11 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_profile_bio_alter_profile_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='dob',
        ),
    ]