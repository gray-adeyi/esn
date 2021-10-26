# Generated by Django 3.2.8 on 2021-10-24 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='email',
            field=models.EmailField(default='hello@example.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='socialaccount',
            name='name',
            field=models.CharField(choices=[('facebook', 'Facebook'), ('instagram', 'Instagram'), ('linkedin', 'LinkedIn'), ('twitter', 'Twitter')], max_length=20),
        ),
    ]
