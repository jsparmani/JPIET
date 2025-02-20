# Generated by Django 2.1.7 on 2019-05-30 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_auto_20190530_0214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infrastructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/infrastructure')),
                ('text', models.TextField()),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
    ]
