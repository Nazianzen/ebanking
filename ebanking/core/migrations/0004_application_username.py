# Generated by Django 3.0.7 on 2020-06-04 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200604_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='username',
            field=models.CharField(default='giddy', max_length=24),
            preserve_default=False,
        ),
    ]