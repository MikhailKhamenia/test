# Generated by Django 4.2.4 on 2023-08-15 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_remove_book_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=None, upload_to='photos/%Y/%m/%d/', verbose_name='Картинка'),
        ),
    ]