# Generated by Django 2.1.7 on 2019-06-02 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0004_auto_20190602_2031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidate',
            options={'ordering': ['application_no']},
        ),
    ]
