# Generated by Django 3.2.11 on 2022-02-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0014_alter_facescan_uploadedimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facescan',
            name='uploadedimage',
            field=models.ImageField(default='0', upload_to='img/%y'),
        ),
    ]
