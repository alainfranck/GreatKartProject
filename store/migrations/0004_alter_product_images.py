# Generated by Django 3.2.14 on 2022-12-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20221005_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(upload_to='home/c1705764c/GreatKartProject/greatkart/static'),
        ),
    ]
