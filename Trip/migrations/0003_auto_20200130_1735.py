# Generated by Django 2.2 on 2020-01-30 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trip', '0002_remove_guide_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourist',
            name='guide',
        ),
        migrations.RemoveField(
            model_name='tourplan',
            name='guide',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='guide',
        ),
    ]
