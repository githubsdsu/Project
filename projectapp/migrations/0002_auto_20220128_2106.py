# Generated by Django 3.2.8 on 2022-01-28 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facescan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Forgot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('mailbox', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('password', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('confirmpassword', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='mail',
            new_name='username',
        ),
        migrations.AddField(
            model_name='signup',
            name='confirmpassword',
            field=models.TextField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='mailbox',
            field=models.TextField(blank=True, default='0', null=True),
        ),
    ]