# Generated by Django 2.0.6 on 2018-08-03 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediumparser', '0004_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='mediumparser.Tag'),
        ),
    ]