# Generated by Django 3.0.7 on 2020-06-12 14:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0002_auto_20200609_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='about_us/'),
            preserve_default=False,
        ),
    ]
