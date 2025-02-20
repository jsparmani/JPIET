# Generated by Django 2.1.7 on 2019-05-31 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0013_auto_20190530_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculties', to='frontend.Department'),
        ),
        migrations.AlterField(
            model_name='lab',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labs', to='frontend.Department'),
        ),
    ]
