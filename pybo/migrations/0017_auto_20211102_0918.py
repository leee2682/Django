# Generated by Django 3.1.3 on 2021-11-02 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0016_auto_20211102_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='hit',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
