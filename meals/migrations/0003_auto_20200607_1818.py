# Generated by Django 3.0.7 on 2020-06-07 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_meals_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='meals',
            options={'verbose_name': 'meal', 'verbose_name_plural': 'meals'},
        ),
    ]
