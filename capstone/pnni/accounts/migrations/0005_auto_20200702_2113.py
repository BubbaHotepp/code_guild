# Generated by Django 3.0.7 on 2020-07-03 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200702_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='/profile_pics/profile_default.jpg', upload_to='profile_pics/'),
        ),
    ]
