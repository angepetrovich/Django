# Generated by Django 4.1.6 on 2023-02-07 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='disch',
            new_name='dish',
        ),
    ]
