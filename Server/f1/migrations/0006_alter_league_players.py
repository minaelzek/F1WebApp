# Generated by Django 4.1.5 on 2023-12-29 01:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f1', '0005_bonusweekendeventpredictionresult_bonus_weekend_prediction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='players',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
