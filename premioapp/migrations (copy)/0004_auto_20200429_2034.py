# Generated by Django 2.1.8 on 2020-04-29 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premioapp', '0003_apkversion'),
    ]

    operations = [
        migrations.AddField(
            model_name='apkversion',
            name='link',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apkversion',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
