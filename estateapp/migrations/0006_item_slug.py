# Generated by Django 3.2.16 on 2022-12-24 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estateapp', '0005_alter_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.CharField(default='real-state', max_length=100, unique=False),
        ),
    ]