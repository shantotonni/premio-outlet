# Generated by Django 2.1.8 on 2020-05-06 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premioapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='outlettype',
            name='code',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='outlettype',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='name',
            field=models.CharField(max_length=70, unique=True),
        ),
    ]
