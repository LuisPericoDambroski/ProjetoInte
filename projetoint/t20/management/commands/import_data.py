def import_item(self, item, config):
    """Importa um item individual para o banco de dados"""
    model = config['model']
    fields_config = config.get('fields', {})
    relations_config = config.get('relations', {})

    # Preparar dados para criação com tratamento de campos obrigatórios
    create_data = {}
    for field, source in fields_config.items():
        if isinstance(source, tuple):  # Campo com valor padrão
            create_data[field] = item.get(source[0], source[1])
        else:
            # Tratamento especial para campos obrigatórios
            if field == 'bonus_defesa' and model == Armadura:
                create_data[field] = item.get(source, 0)  # Valor padrão para armaduras
            else:
                create_data[field] = item.get(source)
                
        # Truncar valores muito longos para campos CharField
        if field in ['classe', 'tipo', 'empunhadura'] and create_data.get(field):
            create_data[field] = create_data[field][:20]

    # Criar/atualizar o objeto principal
    try:
        obj, created = model.objects.update_or_create(
            nome=create_data['nome'],
            defaults=create_data
        )
    except Exception as e:
        self.stdout.write(self.style.ERROR(f'Erro ao salvar {item.get("nome")}: {str(e)}'))
        return

    # Processar relacionamentos com tratamento seguro
    for rel_field, rel_config in relations_config.items():
        try:
            if len(rel_config) == 3:  # ManyToMany
                rel_model, lookup_field, item_field = rel_config
                related_data = item.get(item_field, [])
                if not isinstance(related_data, list):
                    related_data = [related_data] if related_data else []
                
                for rel_item in related_data:
                    rel_obj, _ = rel_model.objects.get_or_create(
                        **{lookup_field: rel_item[:100]}  # Truncar se necessário
                    )
                    getattr(obj, rel_field).add(rel_obj)
                    
            elif len(rel_config) == 2:  # ForeignKey
                rel_model, lookup_field = rel_config
                related_data = item.get(lookup_field)
                if related_data:
                    rel_obj, _ = rel_model.objects.get_or_create(
                        **{lookup_field: related_data[:100]}  # Truncar se necessário
                    )
                    setattr(obj, rel_field, rel_obj)
                    obj.save()
                    
        except Exception as e:
            self.stdout.write(self.style.WARNING(
                f'Erro no relacionamento {rel_field} para {obj.nome}: {str(e)}'
            ))

    # Feedback visual
    action = "Criado" if created else "Atualizado"
    self.stdout.write(self.style.SUCCESS(f'{action}: {obj.nome} ({model.__name__})'))