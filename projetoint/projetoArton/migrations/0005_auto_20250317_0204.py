# Generated by Django 3.1 on 2025-03-17 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetoArton', '0004_customuser_reset_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='reset_token',
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
