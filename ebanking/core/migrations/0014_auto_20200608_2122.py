# Generated by Django 3.0.7 on 2020-06-08 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]