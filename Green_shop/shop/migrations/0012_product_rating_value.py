# Generated by Django 3.2.5 on 2021-08-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_remove_product_rating_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating_value',
            field=models.CharField(max_length=30, null=True, verbose_name='Рейтинг'),
        ),
    ]
