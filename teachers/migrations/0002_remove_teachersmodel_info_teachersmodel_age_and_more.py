# Generated by Django 4.1.7 on 2023-04-03 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachersmodel',
            name='info',
        ),
        migrations.AddField(
            model_name='teachersmodel',
            name='age',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachersmodel',
            name='experience',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachersmodel',
            name='position',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachersmodel',
            name='university',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teachersmodel',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]