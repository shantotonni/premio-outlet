# Generated by Django 2.1.8 on 2020-05-07 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('premioapp', '0002_auto_20200506_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveLocation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=10)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('entry_time', models.DateTimeField()),
                ('server_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='live_location_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Live Location',
                'db_table': 'live_location',
            },
        ),
    ]
