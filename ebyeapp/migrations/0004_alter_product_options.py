# Generated by Django 4.1.7 on 2023-02-18 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ebyeapp', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]