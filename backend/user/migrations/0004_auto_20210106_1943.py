# Generated by Django 3.1.4 on 2021-01-06 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210106_1943'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('id',), 'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
    ]
