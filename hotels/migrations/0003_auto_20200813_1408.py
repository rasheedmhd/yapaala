# Generated by Django 2.1 on 2020-08-13 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_auto_20200813_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='realtors/%Y/%m/%d/'),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
