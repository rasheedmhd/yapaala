# Generated by Django 2.1 on 2020-07-13 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190727_0736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('body', models.TextField()),
                ('more_infor', models.TextField()),
                ('seller', models.CharField(max_length=50)),
                ('land_image', models.ImageField(blank=True, null=True, upload_to='blogging/post/%Y/%m/%d/')),
                ('publish', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
