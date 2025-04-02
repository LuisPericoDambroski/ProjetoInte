# Generated by Django 5.1.7 on 2025-03-30 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t20', '0005_tipopoder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magia',
            name='duracao',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='magia',
            name='resistencia',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='materialespecial',
            name='custo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='materialespecial',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='materialespecial',
            name='modificador',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='materialespecial',
            name='raridade',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='materialespecial',
            name='tipo_item',
            field=models.CharField(default='arma', max_length=50),
        ),
        migrations.AlterField(
            model_name='pericia',
            name='atributo',
            field=models.CharField(choices=[('FOR', 'Força'), ('DES', 'Destreza'), ('CON', 'Constituição'), ('INT', 'Inteligência'), ('SAB', 'Sabedoria'), ('CAR', 'Carisma')], max_length=20),
        ),
    ]
