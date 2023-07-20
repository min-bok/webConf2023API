# Generated by Django 4.2.3 on 2023-07-20 02:47

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
                ('author', models.CharField(max_length=12, verbose_name='작성자')),
                ('post_msg', models.TextField(verbose_name='내용')),
                ('sticker', models.ImageField(blank=True, null=True, upload_to='', verbose_name='스티커')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='작성일')),
            ],
        ),
    ]
