# Generated by Django 4.0.2 on 2022-03-01 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0023_facescan_mailbox'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailbox', models.TextField(blank=True, default='0', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='facescan',
            name='mailbox',
        ),
    ]