# Generated by Django 4.1.3 on 2022-12-02 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_tag_alter_category_options_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
    ]