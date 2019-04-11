# Generated by Django 2.1 on 2019-03-30 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('body', models.TextField()),
                ('writer', models.CharField(max_length=50)),
                ('blog_image', models.ImageField(blank=True, null=True, upload_to='blogging/post/%Y/%m/%d/')),
                ('publish', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
                ('status', models.CharField(choices=[('DRAFT', 'Draft'), ('PUBLISHED', 'Published')], default='DRAFT', max_length=20)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
        migrations.DeleteModel(
            name='Blog_post',
        ),
    ]