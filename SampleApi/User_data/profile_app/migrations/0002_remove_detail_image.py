# Generated by Django 3.0.3 on 2020-03-02 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='Image',
        ),
    ]
