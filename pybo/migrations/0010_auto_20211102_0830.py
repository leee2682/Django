# Generated by Django 3.1.3 on 2021-11-01 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0009_question_hit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='hit',
            field=models.IntegerField(default=0),
        ),
    ]
