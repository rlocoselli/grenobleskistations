# Generated by Django 4.2.4 on 2025-01-01 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_skistation_distancefromgrenoble'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skistation',
            name='altitude',
            field=models.IntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='skistation',
            name='distanceFromGrenoble',
            field=models.IntegerField(default=100),
        ),
    ]
