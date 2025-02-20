# Generated by Django 2.1.7 on 2019-05-31 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0018_exam'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePDF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.PositiveIntegerField(unique=True)),
                ('application_form', models.FileField(upload_to='pdf/home_pdf')),
                ('information_brochure', models.FileField(upload_to='pdf/home_pdf')),
                ('fees', models.FileField(upload_to='pdf/home_pdf')),
                ('aicte', models.FileField(upload_to='pdf/home_pdf')),
                ('anti_ragging', models.FileField(upload_to='pdf/home_pdf')),
                ('training_placement', models.FileField(upload_to='pdf/home_pdf')),
            ],
        ),
    ]
