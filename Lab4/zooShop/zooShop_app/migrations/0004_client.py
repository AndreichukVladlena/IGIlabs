# Generated by Django 4.2.1 on 2023-06-05 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zooShop_app', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Enter first name', max_length=20)),
                ('last_name', models.CharField(help_text='Enter last name', max_length=20)),
                ('date_of_birth', models.DateField(help_text='Enter date of birth')),
                ('email', models.EmailField(help_text='Enter email', max_length=254)),
                ('phone_number', models.CharField(help_text='Enter phone number', max_length=15)),
            ],
        ),
    ]