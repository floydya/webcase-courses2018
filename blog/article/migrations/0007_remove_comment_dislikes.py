# Generated by Django 2.0.7 on 2018-07-28 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20180728_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='dislikes',
        ),
    ]
