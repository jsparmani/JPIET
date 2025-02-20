# Generated by Django 2.1.7 on 2019-05-29 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.PositiveIntegerField(unique=True)),
                ('logo_image', models.ImageField(upload_to='images/logo')),
                ('carousel_image1', models.ImageField(upload_to='images/carousel')),
                ('carousel_image2', models.ImageField(upload_to='images/carousel')),
                ('carousel_image3', models.ImageField(upload_to='images/carousel')),
                ('carousel_image4', models.ImageField(upload_to='images/carousel')),
                ('side_image', models.ImageField(upload_to='images/side')),
            ],
        ),
    ]
