# Generated by Django 2.1.7 on 2019-05-30 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['uid']},
        ),
    ]
