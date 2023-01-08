# Generated by Django 4.0.2 on 2023-01-08 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='phoned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lead',
            name='profile_pics',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='lead',
            name='special_files',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
