# Generated by Django 5.0 on 2024-01-02 00:00

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f1', '0010_alter_league_players'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weekendeventprediction',
            name='circuit',
        ),
        migrations.AddField(
            model_name='qualifiyingresults',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='raceresult',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sprintresult',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sprintshootoutresult',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weekendeventprediction',
            name='race',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='f1.raceresult'),
            preserve_default=False,
        ),
    ]