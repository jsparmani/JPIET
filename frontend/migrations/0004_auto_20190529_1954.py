# Generated by Django 2.1.7 on 2019-05-29 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='images/media_coverage')),
                ('on_landing', models.BooleanField()),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.AlterModelOptions(
            name='notice',
            options={'ordering': ['-pk']},
        ),
    ]
