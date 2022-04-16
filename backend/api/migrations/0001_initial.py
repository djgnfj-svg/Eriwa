# Generated by Django 4.0.4 on 2022-04-16 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ER_Base_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
                ('winning_rate', models.FloatField()),
                ('averageKills', models.FloatField()),
                ('averageHunts', models.FloatField()),
                ('averageDeal', models.FloatField()),
                ('averageProficiency', models.FloatField()),
                ('soloTier', models.CharField(max_length=10)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
