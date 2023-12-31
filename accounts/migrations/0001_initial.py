# Generated by Django 4.2.7 on 2023-12-06 17:37

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(blank=True, default='', max_length=254, unique=True)),
                ('username', models.CharField(blank=True, default='', max_length=255, unique=True)),
                ('surname', models.CharField(max_length=255)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('activate_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Activate code')),
                ('slug', models.SlugField(unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', accounts.models.CustomUserManager()),
            ],
        ),
    ]
