# Generated by Django 2.2.6 on 2019-11-20 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_review2'),
    ]

    operations = [
        migrations.AddField(
            model_name='review2',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]