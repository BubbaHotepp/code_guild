# Generated by Django 3.0.7 on 2020-07-03 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200630_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='profile_pics/profile_default.png', upload_to='profile_pics/'),
        ),
    ]
