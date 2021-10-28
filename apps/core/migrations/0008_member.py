# Generated by Django 3.2.8 on 2021-10-28 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_teamlead_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(help_text='your surname', max_length=100)),
                ('firstname', models.CharField(help_text='your name', max_length=100)),
                ('department', models.CharField(choices=[('civil engr', 'Civil Engineering'), ('mech engr', 'Mechanical Engineering'), ('elect engr', 'Electrical Engineering'), ('Computer engr', 'Computer Engineering')], max_length=50)),
                ('position', models.CharField(default='Nil', max_length=50)),
                ('Team', models.CharField(choices=[(0, 'Media Team'), (1, 'Research Team'), (2, 'Logistics Team'), (3, 'Project Supervision Team'), (4, 'Finance Team'), (5, 'Departmental Team'), (6, 'Design and Creative Team'), (7, 'Purchase Team'), (8, 'Organizing Team'), (9, 'Project Team'), (10, 'Campus Team')], max_length=30)),
                ('passport', models.ImageField(help_text='Strictly your pasport photograph', upload_to='')),
            ],
        ),
    ]
