# Generated by Django 2.2.6 on 2019-10-28 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('critic', models.CharField(default='NULL', max_length=50)),
                ('review', models.TextField(default='NULL', max_length=1000)),
            ],
        ),
    ]