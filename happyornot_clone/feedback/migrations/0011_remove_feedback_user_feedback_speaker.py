# Generated by Django 4.2.1 on 2023-05-14 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speaker', '0002_rename_speker_speaker'),
        ('feedback', '0010_feedback_trainingtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='user',
        ),
        migrations.AddField(
            model_name='feedback',
            name='speaker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='speaker.speaker'),
        ),
    ]
