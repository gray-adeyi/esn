# Generated by Django 3.2.8 on 2021-10-24 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20211024_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamlead',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='team_leads', to='core.site'),
            preserve_default=False,
        ),
    ]