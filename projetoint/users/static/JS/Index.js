document.addEventListener('DOMContentLoaded', function() {
    // Mapeamento completo das características de cada raça
    const racasCaracteristicas = {
        'Anão': {
            movimento: '6 metros',
            tamanho: 'Médio',
            visao: 'Visão no Escuro',
            atributos: 'Constituição +2, Sabedoria +1, Carisma -1'
        },
        'Dahllan': {
            movimento: '9 metros',
            tamanho: 'Médio',
            visao: 'Normal',
            atributos: 'Sabedoria +2, Inteligência +1, Força -1'
        },
        'Elfo': {
            movimento: '9 metros',
            tamanho: 'Médio',
            visao: 'Visão no Escuro',
            atributos: 'Destreza +2, Inteligência +1, Constituição -1'
        },
        'Goblin': {
            movimento: '9 metros',
            tamanho: 'Pequeno',
            visao: 'Visão no Escuro',
            atributos: 'Destreza +2, Carisma +1, Força -1'
        },
        'Golem': {
            movimento: '6 metros',
            tamanho: 'Médio',
            visao: 'Normal',
            atributos: 'Força +2, Constituição +1, Destreza -2'
        },
        'Humano': {
            movimento: '9 metros',
            tamanho: 'Médio',
            visao: 'Normal',
            atributos: '+2 em três atributos diferentes'
        },
        'Hynne': {
            movimento: '9 metros',
            tamanho: 'Pequeno',
            visao: 'Normal',
            atributos: 'Destreza +2, Carisma +1, Força -1'
        },
        'Kliren': {
            movimento: '9 metros',
            tamanho: 'Pequeno',
            visao: 'Visão no Escuro',
            atributos: 'Inteligência +2, Destreza +1, Força -1'
        },
        'Lefou': {
            movimento: '9 metros',
            tamanho: 'Médio',
            visao: 'Normal',
            atributos: '+1 em três atributos diferentes, Carisma -2'
        },
        'Medusa': {
            movimento: '9 metros',
            tamanho: 'Médio',
            visao: 'Visão no Escuro',
            atributos: 'Carisma +2, Destreza +1, Força -2'
        },
        'Minotauro': {
            movimento: '9 metros',
            tamanho: 'Médio',
            visao: 'Normal',
            atributos: 'Força +2, Constituição +1, Inteligência -1'
        },
        'Osteon': {
            movimento: '9 metros',
            tamanho: 'Médio',
            visao: 'Visão no Escuro',
            atributos: '+1 em três atributos diferentes, Constituição -2'
        },
        'Qareen': {
            movimento: '9 metros',
            tamanho: 'Médio',
            visao: 'Normal',
            atributos: 'Carisma +2, Inteligência +1, Força -1'
        },
        'Sílfide': {
            movimento: '6 metros (voando 12m)',
            tamanho: 'Minúsculo',
            visao: 'Visão na Penumbra',
            atributos: 'Carisma +2, Destreza +1, Força -2'
        },
        'Suraggel': {
            movimento: '9 metros (voando 12m)',
            tamanho: 'Médio',
            visao: 'Visão no Escuro',
            atributos: 'Carisma +2, Sabedoria +1, Força -1'
        },
        'Tritão': {
            movimento: '9 metros (nadando 12m)',
            tamanho: 'Médio',
            visao: 'Visão no Escuro',
            atributos: '+1 em três atributos diferentes'
        },
        'Trog': {
            movimento: '9 metros',
            tamanho: 'Médio',
            visao: 'Visão no Escuro',
            atributos: 'Força +2, Constituição +1, Inteligência -1'
        }
    };

    // Elementos do DOM
    const mainRaceImage = document.getElementById('main-race-image');
    const featureSpans = document.querySelectorAll('.caracteristicas span');
    const raceOptions = document.querySelectorAll('.race');

    // Função para atualizar as características exibidas
    function atualizarCaracteristicas(racaId) {
        const caracteristicas = racasCaracteristicas[racaId];
        
        if (caracteristicas) {
            featureSpans[0].textContent = caracteristicas.movimento.toLowerCase();
            featureSpans[1].textContent = caracteristicas.tamanho.toLowerCase();
            featureSpans[2].textContent = caracteristicas.visao.toLowerCase();
            featureSpans[3].textContent = caracteristicas.atributos.toLowerCase();
            
            // Atualiza a imagem da raça selecionada
            const raceImg = document.getElementById(racaId);
            if (raceImg) {
                mainRaceImage.src = raceImg.src;
                mainRaceImage.alt = raceImg.alt;
            }
        }
    }

    // Adiciona eventos de clique para cada opção de raça
    raceOptions.forEach(raceOption => {
        raceOption.addEventListener('click', function() {
            const raceId = this.querySelector('img').id;
            
            // Remove a classe 'active' de todas as opções
            raceOptions.forEach(option => {
                option.classList.remove('active');
            });
            
            // Adiciona a classe 'active' na opção selecionada
            this.classList.add('active');
            
            // Atualiza as características exibidas
            atualizarCaracteristicas(raceId);
        });
    });

    // Seleciona a primeira raça por padrão
    if (raceOptions.length > 0) {
        raceOptions[0].click();
    }

    // Fallback para imagem principal
    mainRaceImage.onerror = function() {
        this.src = 'data:image/svg+xml;charset=UTF-8,%3Csvg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 200 200"%3E%3Crect fill="%23FFD700" width="200" height="200"/%3E%3Ctext fill="%23320000" font-family="Arial" font-size="24" dy=".3em" text-anchor="middle" x="100" y="100"%3ERaça não encontrada%3C/text%3E%3C/svg%3E';
        this.alt = 'Raça não encontrada';
    };
});