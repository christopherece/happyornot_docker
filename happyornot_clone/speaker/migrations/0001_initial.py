# Generated by Django 4.2.1 on 2023-05-12 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('description', models.CharField(blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('is_highrated', models.BooleanField(default=False)),
            ],
        ),
    ]
