# Generated by Django 4.1.6 on 2023-02-14 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0010_alter_category_options_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'CATEGORY', 'verbose_name_plural': 'CATEGORY'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'NEWS', 'verbose_name_plural': 'NEWS'},
        ),
    ]