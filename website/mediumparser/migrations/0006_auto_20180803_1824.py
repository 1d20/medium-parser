# Generated by Django 2.0.6 on 2018-08-03 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediumparser', '0005_auto_20180803_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='mediumparser.Tag'),
        ),
    ]