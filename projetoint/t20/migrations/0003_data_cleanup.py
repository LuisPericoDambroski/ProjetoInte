from django.db import migrations

def truncate_fields(apps, schema_editor):
    models_to_clean = {
        'Acessorio': ['tipo'],
        'Arma': ['classe', 'tipo', 'empunhadura', 'critico'],
        'Armadura': ['classe'],
        'Magia': ['classe'],
    }
    
    for model_name, fields in models_to_clean.items():
        Model = apps.get_model('t20', model_name)
        for item in Model.objects.all():
            for field in fields:
                value = getattr(item, field)
                if value and len(value) > 20:
                    setattr(item, field, value[:20])
            item.save()

class Migration(migrations.Migration):
    dependencies = [
        ('t20', '0002_previous_migration'),
    ]
    
    operations = [
        migrations.RunPython(truncate_fields),
    ]