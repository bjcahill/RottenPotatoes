# Generated by Django 2.2.7 on 2019-11-28 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20191116_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='critic',
            field=models.BooleanField(default=False),
        ),
    ]
