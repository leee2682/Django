# Generated by Django 3.1.3 on 2021-11-05 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0020_auto_20211105_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='hit',
        ),
    ]