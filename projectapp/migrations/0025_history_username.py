# Generated by Django 4.0.2 on 2022-03-01 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0024_history_remove_facescan_mailbox'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='username',
            field=models.TextField(blank=True, default='0', null=True),
        ),
    ]
