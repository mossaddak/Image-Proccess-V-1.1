# Generated by Django 4.2 on 2023-04-22 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_imageprocess_sharpe_png'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageprocess',
            name='filter_img_pdf',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Filter Imag Pdf'),
        ),
    ]