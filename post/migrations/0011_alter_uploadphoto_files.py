# Generated by Django 4.2.3 on 2023-07-28 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_uploadphoto_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadphoto',
            name='files',
            field=models.FileField(null=True, upload_to='%Y/%m/%d'),
        ),
    ]
