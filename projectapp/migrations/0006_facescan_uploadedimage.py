# Generated by Django 3.2.11 on 2022-02-01 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0005_facescan'),
    ]

    operations = [
        migrations.AddField(
            model_name='facescan',
            name='uploadedimage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
