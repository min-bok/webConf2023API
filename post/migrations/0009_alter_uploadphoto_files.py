# Generated by Django 4.2.3 on 2023-07-28 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_alter_uploadphoto_filename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadphoto',
            name='files',
            field=models.ImageField(upload_to='%Y/%m/%d'),
        ),
    ]
