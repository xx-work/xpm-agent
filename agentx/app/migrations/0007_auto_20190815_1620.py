# Generated by Django 2.0.12 on 2019-08-15 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190815_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cronlog',
            name='log_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='log_id'),
        ),
        migrations.AlterField(
            model_name='tasklog',
            name='log_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='log_id'),
        ),
    ]