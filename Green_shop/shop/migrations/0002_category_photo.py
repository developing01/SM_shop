# Generated by Django 3.2.5 on 2021-07-14 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Фото'),
        ),
    ]
