# Generated by Django 3.0.3 on 2020-02-27 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
