# Generated by Django 3.2.11 on 2022-02-01 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0009_alter_facescan_uploadedimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facescan',
            name='uploadedimage',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
