# Generated by Django 4.0.4 on 2022-04-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_er_user_info_model_mmr_alter_er_game_record_mmr_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='er_stats_model',
            name='mmr',
        ),
        migrations.AddField(
            model_name='er_stats_model',
            name='rank',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
