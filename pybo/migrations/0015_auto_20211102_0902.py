# Generated by Django 3.1.3 on 2021-11-02 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0014_question_hit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='hit',
        ),
        migrations.AddField(
            model_name='answer',
            name='hit',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
