# Generated by Django 4.0.2 on 2023-01-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='description',
            field=models.TextField(default='Text'),
        ),
    ]
