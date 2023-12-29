# Generated by Django 4.1.5 on 2023-12-29 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('f1', '0006_alter_league_players'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bonusweekendeventpredictionresult',
            old_name='points_gained',
            new_name='fantasy_points_gained',
        ),
        migrations.RemoveField(
            model_name='bonusweekendprediction',
            name='over',
        ),
        migrations.RemoveField(
            model_name='bonusweekendprediction',
            name='under',
        ),
        migrations.RemoveField(
            model_name='weekendeventprediction',
            name='season',
        ),
        migrations.RemoveField(
            model_name='weekendeventpredictionresult',
            name='points_gained',
        ),
        migrations.AddField(
            model_name='bonusweekendprediction',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='f1.driver'),
        ),
        migrations.AddField(
            model_name='weekendeventpredictionresult',
            name='fantasy_points_gained',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bonusweekendprediction',
            name='prediction',
            field=models.BooleanField(null=True),
        ),
    ]
