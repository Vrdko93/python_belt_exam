# Generated by Django 2.2.4 on 2020-04-25 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('handy_helper_app', '0005_auto_20200424_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='uploaded_by',
            new_name='uploaded_b',
        ),
    ]
