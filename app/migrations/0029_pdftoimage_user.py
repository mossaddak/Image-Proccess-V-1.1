# Generated by Django 4.1.7 on 2023-04-23 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0028_alter_imageprocess_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdftoimage',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pdf_to_image', to=settings.AUTH_USER_MODEL),
        ),
    ]
