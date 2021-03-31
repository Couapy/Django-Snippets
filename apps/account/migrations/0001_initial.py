# Generated by Django 3.0.8 on 2021-03-13 13:50

import account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biography', models.TextField(blank=True, help_text='300 characters maximum', max_length=300, null=True, verbose_name='Biography')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Web site')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=account.models.user_directory_path, verbose_name='Profil picture')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]