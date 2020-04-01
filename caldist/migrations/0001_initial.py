# Generated by Django 2.0.13 on 2020-03-26 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('longname', models.CharField(max_length=100, verbose_name='Name')),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=8, verbose_name='Latitude')),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=8, verbose_name='longitude')),
            ],
        ),
    ]
