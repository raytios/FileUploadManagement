# Generated by Django 3.0.6 on 2020-05-17 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_auto_20200517_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborate_files_a00',
            name='category',
            field=models.CharField(choices=[('IMAGE', 'Image'), ('AUDIO', 'Audio'), ('VIDEO', 'Video'), ('DOCUMENT', 'Document')], max_length=20),
        ),
    ]