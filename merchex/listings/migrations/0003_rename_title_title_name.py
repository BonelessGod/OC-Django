# Generated by Django 4.1 on 2022-09-02 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='title',
            old_name='title',
            new_name='name',
        ),
    ]
