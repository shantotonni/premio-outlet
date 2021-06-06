# Generated by Django 2.1.8 on 2020-05-06 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApkVersion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('version', models.IntegerField()),
                ('version_text', models.CharField(max_length=10)),
                ('link', models.TextField()),
            ],
            options={
                'verbose_name': 'Apk Version',
                'db_table': 'apk_version',
            },
        ),
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('code', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'Base',
                'db_table': 'base',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('code', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('code', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'Department',
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('code', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'Designation',
                'db_table': 'designation',
            },
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'Market',
                'db_table': 'market',
            },
        ),
        migrations.CreateModel(
            name='Outlet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('propritor_name', models.CharField(max_length=100, unique=True)),
                ('mobile', models.CharField(max_length=20)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='outlet_category', to='premioapp.Category')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='outlet_creator', to=settings.AUTH_USER_MODEL)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='outlet_market', to='premioapp.Market')),
            ],
            options={
                'verbose_name': 'Outlet',
                'db_table': 'outlet',
            },
        ),
        migrations.CreateModel(
            name='OutletType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('code', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'Outlet Type',
                'db_table': 'outlet_type',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('code', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'Region',
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='base_routes', to='premioapp.Base')),
            ],
            options={
                'verbose_name': 'Route',
                'db_table': 'route',
            },
        ),
        migrations.CreateModel(
            name='RouteDay',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'Route Day',
                'db_table': 'route_day',
            },
        ),
        migrations.CreateModel(
            name='UserBase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_base_base', to='premioapp.Base')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_base_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Base',
                'db_table': 'user_base',
            },
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_detail_department', to='premioapp.Department')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_detail_designation', to='premioapp.Designation')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_details', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Detail',
                'db_table': 'user_detail',
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='zone_region', to='premioapp.Region')),
            ],
            options={
                'verbose_name': 'Zone',
                'db_table': 'zone',
            },
        ),
        migrations.AddField(
            model_name='route',
            name='route_day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='route_day_routes', to='premioapp.RouteDay'),
        ),
        migrations.AddField(
            model_name='outlet',
            name='outlet_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='outlet_outlet_type', to='premioapp.OutletType'),
        ),
        migrations.AddField(
            model_name='market',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='route_markets', to='premioapp.Route'),
        ),
        migrations.AddField(
            model_name='base',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='base_zone', to='premioapp.Zone'),
        ),
        migrations.AlterUniqueTogether(
            name='userbase',
            unique_together={('user', 'base')},
        ),
        migrations.AlterUniqueTogether(
            name='route',
            unique_together={('base', 'name', 'route_day')},
        ),
        migrations.AlterUniqueTogether(
            name='outlet',
            unique_together={('name', 'propritor_name', 'mobile')},
        ),
    ]