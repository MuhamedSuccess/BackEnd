# Generated by Django 2.2 on 2020-01-30 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trip', '0005_auto_20200130_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
