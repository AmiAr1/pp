# Generated by Django 4.1.1 on 2022-09-30 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dorama', '0002_dorama_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dorama',
            name='image',
            field=models.ImageField(blank=True, upload_to='dorams/%Y/%m/%d', verbose_name='Изображение'),
        ),
    ]
