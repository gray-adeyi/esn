# Generated by Django 3.2.8 on 2021-10-28 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='Team',
            new_name='team',
        ),
    ]
