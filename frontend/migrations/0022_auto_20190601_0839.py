# Generated by Django 2.1.7 on 2019-06-01 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0021_auto_20190601_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syllabus',
            name='semester',
            field=models.ForeignKey(on_delete='models.CASCADE', related_name='syllabus', to='frontend.Semester'),
        ),
    ]
