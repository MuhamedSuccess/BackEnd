# Generated by Django 2.2 on 2020-01-30 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200130_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='birth date'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_admin',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_guide',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_tourist',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
