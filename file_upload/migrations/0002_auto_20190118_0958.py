# Generated by Django 2.1.5 on 2019-01-18 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='coordinates',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
