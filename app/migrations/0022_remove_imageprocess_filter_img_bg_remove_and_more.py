# Generated by Django 4.1.7 on 2023-04-22 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_imageprocess_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageprocess',
            name='filter_img_bg_remove',
        ),
        migrations.AddField(
            model_name='imageprocess',
            name='bg_remove',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Background Removed Image'),
        ),
    ]
