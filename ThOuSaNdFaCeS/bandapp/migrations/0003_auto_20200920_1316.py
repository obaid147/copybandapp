# Generated by Django 3.1 on 2020-09-20 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandapp', '0002_auto_20200920_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='Mp3',
            field=models.FileField(upload_to='fans_files/mp3/'),
        ),
    ]
