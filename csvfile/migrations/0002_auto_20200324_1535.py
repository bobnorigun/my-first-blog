# Generated by Django 2.0.13 on 2020-03-24 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csvfile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Profile',
            new_name='profile',
        ),
    ]
