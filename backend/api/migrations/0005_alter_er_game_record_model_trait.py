# Generated by Django 4.0.4 on 2022-05-09 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_er_stats_model_averageitem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='er_game_record_model',
            name='Trait',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.traitmodel'),
        ),
    ]