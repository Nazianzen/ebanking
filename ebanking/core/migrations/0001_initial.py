# Generated by Django 3.0.6 on 2020-05-29 15:40

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiary_name', models.CharField(max_length=64)),
                ('beneficiary_phone', models.CharField(max_length=15)),
                ('beneficiary_address', models.CharField(max_length=255)),
                ('beneficiary_email', models.EmailField(max_length=254)),
                ('beneficiary_bank', models.CharField(max_length=64)),
                ('beneficiary_account', models.IntegerField()),
                ('swift', models.CharField(max_length=24)),
                ('iban', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('state', models.CharField(max_length=36)),
                ('city', models.CharField(max_length=36)),
                ('marital_status', models.CharField(choices=[('S', 'Single'), ('M', 'Married'), ('D', 'Divorced')], max_length=1)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('pin', models.IntegerField()),
                ('image', models.ImageField(height_field=300, upload_to='profile_pics', width_field=300)),
                ('ip_address', models.GenericIPAddressField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_ref', models.CharField(default=core.models.generate_transaction_ref, max_length=16)),
                ('transaction_amount', models.FloatField()),
                ('transaction_fee', models.FloatField()),
                ('transaction_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('beneficiary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Beneficiary')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=64)),
                ('account_number', models.IntegerField()),
                ('account_type', models.CharField(choices=[('S', 'Savings'), ('C', 'Current'), ('F', 'Fixed Deposit')], max_length=1)),
                ('account_balance', models.FloatField()),
                ('tac', models.CharField(default=core.models.generate_random_digits, max_length=4)),
                ('tax', models.CharField(default=core.models.generate_random_digits, max_length=4)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]