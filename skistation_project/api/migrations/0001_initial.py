# Generated by Django 4.2.4 on 2024-12-15 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SkiStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('capacity', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkiCircuit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(max_length=20)),
                ('num_pistes', models.IntegerField()),
                ('ski_station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.skistation')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('type', models.CharField(max_length=50)),
                ('opening_hours', models.CharField(max_length=100, null=True)),
                ('ski_station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.skistation')),
            ],
        ),
        migrations.CreateModel(
            name='BusLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_number', models.CharField(max_length=50)),
                ('departure_stop', models.CharField(max_length=100)),
                ('arrival_stop', models.CharField(max_length=100)),
                ('frequency', models.CharField(max_length=50, null=True)),
                ('travel_time', models.CharField(max_length=50, null=True)),
                ('ski_station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.skistation')),
            ],
        ),
    ]
