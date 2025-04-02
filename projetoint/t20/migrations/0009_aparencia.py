# Generated by Django 5.1.7 on 2025-03-30 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t20', '0008_delete_aparencia_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aparencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, unique=True)),
                ('tipo', models.CharField(choices=[('fisica', 'Física'), ('vestimenta', 'Vestimenta'), ('marcas', 'Marcas/Cicatrizes'), ('estilo', 'Estilo'), ('outros', 'Outros')], default='fisica', help_text='Tipo de aparência física', max_length=20)),
                ('origem', models.CharField(blank=True, choices=[('T20', 'Tormenta 20'), ('Ghanor', 'Ghanor'), ('Ameacas', 'Ameaças de Arton'), ('Deuses', 'Deuses e Heróis')], default='T20', max_length=20)),
                ('modificadores', models.JSONField(blank=True, default=dict, help_text='Modificadores opcionais que esta aparência pode conceder')),
            ],
            options={
                'verbose_name': 'Aparência',
                'verbose_name_plural': 'Aparências',
                'ordering': ['tipo', 'descricao'],
            },
        ),
    ]
