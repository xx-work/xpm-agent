# Generated by Django 2.0.12 on 2019-08-15 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190815_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cronlog',
            name='job_id',
            field=models.CharField(max_length=255, verbose_name='job_id'),
        ),
    ]