# Generated by Django 4.2 on 2023-04-22 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_imageprocess_filter_img_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageprocess',
            name='filter_img_bg_remove',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Filter Removed Background Image'),
        ),
        migrations.AddField(
            model_name='imageprocess',
            name='filter_img_pdf',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Filter Imag Pdf'),
        ),
    ]
