# Generated by Django 2.1.8 on 2020-04-29 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premioapp', '0002_auto_20200420_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApkVersion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10, unique=True)),
                ('version', models.IntegerField()),
                ('version_text', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Apk Version',
                'db_table': 'apk_version',
            },
        ),
    ]
