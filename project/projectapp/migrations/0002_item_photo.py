# Generated by Django 4.0.5 on 2022-06-16 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='commu_photo'),
        ),
    ]