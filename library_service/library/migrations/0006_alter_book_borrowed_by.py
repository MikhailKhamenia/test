# Generated by Django 4.2.4 on 2023-08-14 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_book_borrowed_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='borrowed_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='library.reader'),
        ),
    ]
