# Generated by Django 2.1.7 on 2019-06-01 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0020_semester'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='semester',
            options={'ordering': ['semester']},
        ),
    ]
