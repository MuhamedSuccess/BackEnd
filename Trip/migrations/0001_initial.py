# Generated by Django 2.2 on 2020-01-30 15:19

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0003_auto_20200130_1538'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'guide',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('check_in_date', models.DateTimeField()),
                ('check_out_date', models.DateTimeField()),
                ('no_of_days', models.IntegerField()),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip', to='Trip.Guide')),
            ],
        ),
        migrations.CreateModel(
            name='TourPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trip.Guide')),
            ],
        ),
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trip.Guide')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.UserProfile')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trip.Trip')),
            ],
            options={
                'db_table': 'tourist',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateTimeField()),
                ('check_out_date', models.DateTimeField()),
                ('event', models.TextField()),
                ('date', models.DateTimeField(blank=True, default=None, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trip.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trip.Trip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
