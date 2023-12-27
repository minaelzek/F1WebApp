# Generated by Django 4.1.5 on 2023-12-27 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('f1', '0006_alter_raceresult_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raceresultdriver',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f1.driver'),
        ),
        migrations.AlterField(
            model_name='raceresultdriver',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]
