# Generated by Django 4.2.1 on 2023-05-12 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speaker', '0002_rename_speker_speaker'),
        ('feedback', '0005_feedback_feedback_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='speaker_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='speaker.speaker'),
            preserve_default=False,
        ),
    ]
