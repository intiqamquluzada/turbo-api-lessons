# Generated by Django 4.2.7 on 2023-11-29 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turbo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ('-created_at',), 'verbose_name': 'Car', 'verbose_name_plural': 'Cars'},
        ),
    ]