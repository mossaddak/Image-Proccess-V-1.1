# Generated by Django 4.1.7 on 2023-04-22 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_remove_imageprocess_filter_img_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageprocess',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Pdf'),
        ),
    ]
