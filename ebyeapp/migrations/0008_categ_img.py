# Generated by Django 4.1.7 on 2023-02-19 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebyeapp', '0007_alter_categ_options_categ_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='categ',
            name='img',
            field=models.ImageField(default='category_images/categ_img.jpg', upload_to='category_images'),
            preserve_default=False,
        ),
    ]