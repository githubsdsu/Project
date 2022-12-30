# Generated by Django 4.0.2 on 2022-02-24 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0021_alter_facescan_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forgot',
            name='mailbox',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='forgot',
            name='username',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='otp',
            name='otp',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='result',
            name='username',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='signup',
            name='firstname',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='signup',
            name='lastname',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='signup',
            name='username',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='update',
            name='confirmpassword',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='update',
            name='password',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='update',
            name='username',
            field=models.TextField(default=None),
        ),
    ]