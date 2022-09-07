# Generated by Django 4.1 on 2022-09-07 11:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_rename_title_title_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='band',
            name='biography',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('R', 'Rock'), ('P', 'Pop'), ('C', 'Country'), ('J', 'Jazz'), ('B', 'Blues'), ('M', 'Metal'), ('O', 'Other'), ('H', 'Hip Hop'), ('S', 'Synth Pop'), ('A', 'Alternative Rock')], default='H', max_length=5),
        ),
        migrations.AddField(
            model_name='band',
            name='official_website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='band',
            name='year_formed',
            field=models.IntegerField(default=2020, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2022)]),
        ),
    ]