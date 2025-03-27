# Generated by Django 3.0.4 on 2025-03-27 19:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('t20', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='acessorio',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='alquimico',
            name='duracao',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='alquimico',
            name='efeito',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='alquimico',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='arma',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='t20.MaterialEspecial'),
        ),
        migrations.AddField(
            model_name='arma',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='armadilha',
            name='gatilho',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='armadilha',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='armadura',
            name='modificadores',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='armadura',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='condicao',
            name='cura',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doenca',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='doenca',
            name='tempo_incubacao',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='esoterico',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='esoterico',
            name='requisitos',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='itemgeral',
            name='categoria',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='magia',
            name='aprimoramentos',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='materialespecial',
            name='tipo_item',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='melhoria',
            name='requisitos',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='poder',
            name='deuses',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='veiculo',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='veiculo',
            name='tripulacao',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='poder',
            name='tipo',
            field=models.CharField(choices=[('combate', 'Combate'), ('destino', 'Destino'), ('magia', 'Magia'), ('concedido', 'Concedido')], max_length=20),
        ),
    ]
