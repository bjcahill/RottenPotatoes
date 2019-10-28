# Generated by Django 2.2.6 on 2019-10-27 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('title', models.CharField(default='NULL', max_length=100, primary_key=True, serialize=False)),
                ('director', models.CharField(default='NULL', max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('star', models.CharField(default='NULL', max_length=100)),
                ('score', models.FloatField(default=0)),
                ('runTime', models.IntegerField(default=0)),
                ('rating', models.CharField(choices=[('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17')], default='G', max_length=5)),
                ('releaseDate', models.DateField(default='1900-01-01')),
                ('studio', models.CharField(default='NULL', max_length=100)),
            ],
        ),
    ]
