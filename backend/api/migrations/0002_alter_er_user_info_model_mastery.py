# Generated by Django 4.0.4 on 2022-04-25 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='er_user_info_model',
            name='mastery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mastery', to='api.mastery'),
        ),
    ]