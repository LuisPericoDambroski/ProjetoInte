document.addEventListener('DOMContentLoaded', () => {
    // =============================================
    // 1. GERENCIAMENTO DO DROPDOWN (PERFIL)
    // =============================================
    const dropdownToggle = document.querySelector('.dropdown-toggle');
    const dropdownMenu = document.querySelector('.dropdown-menu');
    
    if (dropdownToggle && dropdownMenu) {
        // Função para fechar o dropdown quando clicar fora
        const handleClickOutside = (e) => {
            if (!dropdownToggle.contains(e.target) && !dropdownMenu.contains(e.target)) {
                dropdownMenu.style.display = 'none';
                document.removeEventListener('click', handleClickOutside);
            }
        };
        
        // Abrir/fechar dropdown
        dropdownToggle.addEventListener('click', (e) => {
            e.stopPropagation();
            const isOpen = dropdownMenu.style.display === 'block';
            dropdownMenu.style.display = isOpen ? 'none' : 'block';
            
            if (!isOpen) {
                // Adiciona o listener com pequeno delay para evitar conflito imediato
                setTimeout(() => {
                    document.addEventListener('click', handleClickOutside);
                }, 10);
            }
        });
    }

    // =============================================
    // 2. SISTEMA DE SELEÇÃO DE RAÇAS
    // =============================================
    const mainRaceImage = document.querySelector('.Icon img');
    const caracteristicasDiv = document.querySelector('.caracteristicas');
    const spans = caracteristicasDiv?.querySelectorAll('span');

    // Mapeamento completo das características das raças
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
        'Suraggel (Aggelus)': {
            movimento: '9 metros (voando 12m)',
            tamanho: 'Médio',
            visao: 'Visão no Escuro',
            atributos: 'Carisma +2, Sabedoria +1, Força -1'
        },
        'Suraggel (Sulfure)': {
            movimento: '9 metros (voando 12m)',
            tamanho: 'Médio',
            visao: 'Visão no Escuro',
            atributos: 'Força +2, Constituição +1, Carisma -1'
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

    // Função para atualizar as características exibidas
    const atualizarCaracteristicas = (racaId) => {
        if (!spans || !racasCaracteristicas[racaId]) return;
        
        const { movimento, tamanho, visao, atributos } = racasCaracteristicas[racaId];
        spans[0].textContent = movimento;
        spans[1].textContent = tamanho.toLowerCase();
        spans[2].textContent = visao.toLowerCase();
        spans[3].textContent = atributos.toLowerCase();
    };

    // Event delegation para os cliques nas raças
    document.querySelector('.races-icons')?.addEventListener('click', (e) => {
        const raceDiv = e.target.closest('.race');
        if (!raceDiv) return;

        const img = raceDiv.querySelector('img');
        if (!img) return;

        const raceId = img.id;
        
        // Atualiza a imagem principal
        if (mainRaceImage) {
            mainRaceImage.src = `/static/imagens/Icons/Races/${raceId}.png`;
            console.log('Raça selecionada:', raceId);
        }
        
        // Atualiza as características
        atualizarCaracteristicas(raceId);
        
        // Atualiza o estado ativo
        document.querySelectorAll('.races-icons .race').forEach(div => {
            div.classList.toggle('active', div === raceDiv);
        });
        
        // Previne a propagação para não interferir com outros eventos
        e.stopPropagation();
    });

    // Seleciona a primeira raça por padrão
    const primeiraRace = document.querySelector('.races-icons .race');
    if (primeiraRace) {
        primeiraRace.click();
    }
});