# Generated by Django 3.2.14 on 2022-10-24 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=100)),
                ('resume', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=10000)),
                ('image', models.ImageField(null=True, upload_to='media/')),
            ],
        ),
    ]
