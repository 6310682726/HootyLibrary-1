# Generated by Django 4.1 on 2022-10-22 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_models', '0003_alter_user_age_alter_user_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='profile_pic/<django.db.models.fields.CharField>'),
        ),
    ]