# Generated by Django 3.0.7 on 2020-06-30 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photograph',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/'),
        ),
    ]