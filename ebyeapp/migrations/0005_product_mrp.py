# Generated by Django 4.1.7 on 2023-02-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebyeapp', '0004_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mrp',
            field=models.IntegerField(default=999),
            preserve_default=False,
        ),
    ]