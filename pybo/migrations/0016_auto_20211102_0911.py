# Generated by Django 3.1.3 on 2021-11-02 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0015_auto_20211102_0902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='hit',
        ),
        migrations.AddField(
            model_name='question',
            name='hit',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
