# Generated by Django 4.0.4 on 2022-05-27 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='gallery_image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
