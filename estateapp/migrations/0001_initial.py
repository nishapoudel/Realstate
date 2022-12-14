# Generated by Django 4.0.6 on 2022-08-27 16:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Filter_Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(choices=[('Less than 50 Lacs', 'Less than 50 Lacs'), ('50 Lacs - 1 Crore ', '50 Lacs - 1 Crore '), ('1 Crore - 3 Crores', '1 Crore - 3 Crores'), ('3 Crores - 5 Crores', '3 Crores - 5 Crores'), ('5 Crores - 10 Crores', '5 Crores - 10 Crores'), ('10 Crores - 100 Crores', '10 Crores - 100 Crores')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('area', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_date', models.DateField(default=datetime.datetime.now)),
                ('category', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='estateapp.category')),
                ('filter_price', models.ForeignKey(default='50 lakhs', null=True, on_delete=django.db.models.deletion.CASCADE, to='estateapp.filter_price')),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
    ]
