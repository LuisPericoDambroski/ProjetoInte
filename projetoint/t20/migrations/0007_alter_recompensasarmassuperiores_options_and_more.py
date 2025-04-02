# Generated by Django 5.1.7 on 2025-03-30 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t20', '0006_alter_magia_duracao_alter_magia_resistencia_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recompensasarmassuperiores',
            options={'verbose_name': 'Poder', 'verbose_name_plural': 'Poderes'},
        ),
        migrations.RemoveField(
            model_name='poder',
            name='requisitos',
        ),
        migrations.AddField(
            model_name='poder',
            name='custo_pm',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='poder',
            name='magia',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poder',
            name='requisito_carisma',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='poder',
            name='requisito_constituicao',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='poder',
            name='requisito_destreza',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='poder',
            name='requisito_forca',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='poder',
            name='requisito_inteligencia',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='poder',
            name='requisito_nivel',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='poder',
            name='requisito_outros',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='poder',
            name='requisito_pericias',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='poder',
            name='requisito_poderes',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='poder',
            name='requisito_sabedoria',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterModelTable(
            name='recompensasarmassuperiores',
            table=None,
        ),
    ]
