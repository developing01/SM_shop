# Generated by Django 3.2.5 on 2021-08-03 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20210730_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating_value',
            field=models.CharField(max_length=30, null=True, verbose_name='Рейтинг'),
        ),
    ]