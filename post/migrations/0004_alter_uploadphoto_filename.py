# Generated by Django 4.2.3 on 2023-07-28 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_uploadphoto_filename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadphoto',
            name='fileName',
            field=models.CharField(max_length=10, verbose_name='작성자'),
        ),
    ]