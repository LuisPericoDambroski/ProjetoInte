# Generated by Django 5.1.7 on 2025-03-30 04:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t20', '0002_alter_estatisticacriaturasolo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recompensasarmaduras',
            options={'verbose_name': 'Recompensa de Armadura', 'verbose_name_plural': 'Recompensas de Armaduras'},
        ),
        migrations.AlterModelOptions(
            name='recompensasarmadurassuperiores',
            options={'verbose_name': 'Recompensa de Armadura Superior', 'verbose_name_plural': 'Recompensas de Armaduras Superiores'},
        ),
        migrations.RemoveField(
            model_name='materialespecialpreco',
            name='id',
        ),
        migrations.AlterField(
            model_name='arma',
            name='ameaca',
            field=models.CharField(blank=True, help_text="Valor mínimo no d20 para ameaça de crítico (ex: 19, 20 ou '—')", max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='magia',
            name='alcance',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='magia',
            name='duracao',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='magia',
            name='resistencia',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='materialespecialpreco',
            name='material',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='precos', serialize=False, to='t20.materialespecial'),
        ),
    ]
