# Generated by Django 4.2.3 on 2023-07-28 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_remove_uploadphoto_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadphoto',
            name='files',
            field=models.ImageField(upload_to=''),
        ),
    ]
