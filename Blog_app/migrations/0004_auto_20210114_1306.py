# Generated by Django 3.1.2 on 2021-01-14 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_app', '0003_auto_20210114_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile/child.jpg', null=True, upload_to='profile'),
        ),
    ]
