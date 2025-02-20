# Generated by Django 2.1.7 on 2019-05-29 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_statistics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('pdf', models.FileField(upload_to='pdf/notices')),
                ('on_landing', models.BooleanField()),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
