# Generated by Django 3.0.7 on 2020-06-07 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200606_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]