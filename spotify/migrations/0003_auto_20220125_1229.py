# Generated by Django 3.1.6 on 2022-01-25 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0002_auto_20220125_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotifytoken',
            name='expires_in',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
