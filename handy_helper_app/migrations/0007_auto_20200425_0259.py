# Generated by Django 2.2.4 on 2020-04-25 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('handy_helper_app', '0006_auto_20200425_0256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='uploaded_b',
            new_name='uploaded_by',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='users',
            new_name='user',
        ),
    ]
