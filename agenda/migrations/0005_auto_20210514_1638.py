# Generated by Django 2.2 on 2021-05-14 13:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_auto_20210514_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='agenda_visibility',
            field=models.CharField(choices=[('private', 'private'), ('public', 'public')], default='private', max_length=7),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='notify_me_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 15, 6, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='tags',
            field=models.CharField(default='My Tag', max_length=10),
        ),
    ]
