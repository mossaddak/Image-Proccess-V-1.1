# Generated by Django 4.2 on 2023-04-22 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_imageprocess_filter_img_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageprocess',
            name='filter_img_pdf',
        ),
    ]
