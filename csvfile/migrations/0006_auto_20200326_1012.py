# Generated by Django 2.0.13 on 2020-03-26 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvfile', '0005_auto_20200325_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='longitude',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default=11, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default=11, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default=11, max_length=150, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='profile',
            field=models.TextField(default=11),
            preserve_default=False,
        ),
    ]
