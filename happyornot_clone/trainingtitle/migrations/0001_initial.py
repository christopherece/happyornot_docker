# Generated by Django 4.2.1 on 2023-05-14 01:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainingtitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('training_date', models.DateField(default=datetime.datetime.now)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
