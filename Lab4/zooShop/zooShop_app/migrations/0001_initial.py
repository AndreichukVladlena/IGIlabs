# Generated by Django 4.2.1 on 2023-06-05 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(help_text='Enter type', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name', max_length=20)),
                ('address', models.CharField(help_text='Enter owner', max_length=20)),
                ('phone_number', models.CharField(help_text='Enter phone number', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_code', models.CharField(help_text='Enter vendor code', max_length=20)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(help_text='Enter name', max_length=20)),
                ('description', models.TextField(help_text='Enter description')),
                ('cost', models.IntegerField()),
                ('photo', models.ImageField(blank=True, upload_to='images')),
                ('product_type', models.ForeignKey(help_text='Choose product type', null=True, on_delete=django.db.models.deletion.SET_NULL, to='zooShop_app.producttype')),
                ('provider', models.ForeignKey(help_text='Choose provider', null=True, on_delete=django.db.models.deletion.SET_NULL, to='zooShop_app.provider')),
            ],
        ),
    ]
