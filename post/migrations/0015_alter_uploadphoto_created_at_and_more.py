# Generated by Django 4.2.3 on 2023-07-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_uploadphoto_created_at_uploadphoto_filename_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadphoto',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='촬영일'),
        ),
        migrations.AlterField(
            model_name='uploadphoto',
            name='fileName',
            field=models.CharField(default='name', max_length=30, verbose_name='이미지명'),
        ),
        migrations.AlterField(
            model_name='uploadphoto',
            name='files',
            field=models.TextField(default='fiel', verbose_name='이미지 base64'),
        ),
    ]