# Generated by Django 4.0.6 on 2022-08-04 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_area_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='post/img'),
        ),
    ]
