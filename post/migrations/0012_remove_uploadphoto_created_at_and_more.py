# Generated by Django 4.2.3 on 2023-07-28 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_alter_uploadphoto_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadphoto',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='uploadphoto',
            name='fileName',
        ),
        migrations.AlterField(
            model_name='uploadphoto',
            name='files',
            field=models.FileField(upload_to=''),
        ),
    ]
