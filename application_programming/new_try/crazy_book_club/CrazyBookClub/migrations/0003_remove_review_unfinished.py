# Generated by Django 4.2.7 on 2023-11-14 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CrazyBookClub', '0002_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='unfinished',
        ),
    ]
