# Generated by Django 3.0.5 on 2020-04-19 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='artist_name',
            field=models.TextField(default=''),
        ),
    ]