# Generated by Django 3.2.4 on 2021-08-03 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Maqola nomi')),
                ('body', models.CharField(max_length=300, verbose_name='Maydon')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='*')),
                ('image', models.ImageField(upload_to='Maqolalar_rasmi/', verbose_name='Maqola rasmi')),
            ],
            options={
                'verbose_name': 'Maqola',
                'verbose_name_plural': 'Maqolalar',
            },
        ),
    ]