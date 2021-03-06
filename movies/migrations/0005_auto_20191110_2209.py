# Generated by Django 2.2.6 on 2019-11-11 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='id',
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, default='omegalul.png', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='review',
            name='critic',
            field=models.CharField(default='NULL', max_length=50, primary_key=True, serialize=False),
        ),
    ]
