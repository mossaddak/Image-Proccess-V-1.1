# Generated by Django 4.2 on 2023-04-21 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_imageproccess_imageprocess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageprocess',
            name='input',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Input'),
        ),
        migrations.AlterField(
            model_name='imageprocess',
            name='output',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Output'),
        ),
    ]