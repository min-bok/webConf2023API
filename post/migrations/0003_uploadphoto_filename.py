# Generated by Django 4.2.3 on 2023-07-28 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_uploadphoto_alter_post_author_alter_post_post_msg'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadphoto',
            name='fileName',
            field=models.CharField(default='', max_length=10, verbose_name='작성자'),
        ),
    ]