# Generated by Django 3.1 on 2025-03-17 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetoArton', '0005_auto_20250317_0204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='last_login',
        ),
        migrations.AddField(
            model_name='customuser',
            name='reset_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
