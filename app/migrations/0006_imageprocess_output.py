# Generated by Django 4.2 on 2023-04-21 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_imageprocess_output'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageprocess',
            name='output',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Output'),
        ),
    ]
