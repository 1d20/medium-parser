# Generated by Django 2.0.6 on 2018-07-23 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediumparser', '0002_auto_20180623_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.URLField(max_length=255),
        ),
    ]
