# Generated by Django 4.2 on 2023-04-21 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_output_imageprocess_jpg'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageprocess',
            name='png',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Png'),
        ),
    ]
