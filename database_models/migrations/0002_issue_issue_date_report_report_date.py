# Generated by Django 4.1 on 2022-10-23 08:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('database_models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='issue_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='report',
            name='report_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]