# Generated by Django 3.0.7 on 2020-06-09 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0007_auto_20200609_1825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meals',
            old_name='spcialty',
            new_name='specialty',
        ),
    ]
