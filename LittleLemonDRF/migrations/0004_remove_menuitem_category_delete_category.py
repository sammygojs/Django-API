# Generated by Django 4.1.7 on 2023-02-14 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonDRF', '0003_alter_menuitem_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
