# Generated by Django 2.2.7 on 2019-11-17 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_usermodel_join_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='email',
            field=models.CharField(default='NULL', max_length=254),
        ),
    ]