# Generated by Django 4.2 on 2023-04-21 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageproccess',
            name='input',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Input'),
        ),
        migrations.AlterField(
            model_name='imageproccess',
            name='output',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Output'),
        ),
    ]