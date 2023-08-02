# Generated by Django 4.2.2 on 2023-08-02 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=10, verbose_name='작성자')),
                ('post_msg', models.TextField(max_length=100, verbose_name='내용')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='작성일')),
            ],
        ),
        migrations.CreateModel(
            name='UploadPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(default='name', max_length=30, verbose_name='이미지명')),
                ('files', models.FileField(default='files', upload_to='images', verbose_name='이미지')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='촬영일')),
            ],
        ),
    ]