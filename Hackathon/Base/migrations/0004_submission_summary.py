# Generated by Django 4.1.5 on 2023-04-20 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0003_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='summary',
            field=models.TextField(default=' '),
        ),
    ]
