document.addEventListener('DOMContentLoaded', function() {
    // Mapeamento das raças e suas características
    const racasCaracteristicas = {
        'Anão': {
            movimento: '6 metros',
            tamanho: 'Médio',
            visao: 'Visão no Escuro',
            atributos: 'Constituição +2, Sabedoria +1, Carisma -1'
        },
        'Dhallan': {
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
        'Humano': {
            movimento: '9 metros',
            tamanho: 'Médio',
            visao: 'Normal',
            atributos: 'Qualquer atributo +2'
        },
        'Sílfide': {
            movimento: '6 metros (voando 12m)',
            tamanho: 'Minúsculo',
            visao: 'Penumbra',
            atributos: 'Carisma +2, Destreza +1, Força -2'
        }
        // Adicione as outras raças seguindo o mesmo padrão...
    };

    // Elementos do DOM
    const mainRaceImage = document.querySelector('.Icon img');
    const caracteristicasDiv = document.querySelector('.caracteristicas');
    const spans = caracteristicasDiv.querySelectorAll('span');

    // Função para atualizar características
    function atualizarCaracteristicas(racaId) {
        const caracteristicas = racasCaracteristicas[racaId];

        if (caracteristicas) {
            spans[0].textContent = caracteristicas.movimento;
            spans[1].textContent = caracteristicas.tamanho.toLowerCase();
            spans[2].textContent = caracteristicas.visao.toLowerCase();
            spans[3].textContent = caracteristicas.atributos.toLowerCase();
        } else {
            // Reset para valores padrão ou vazio
            spans[0].textContent = '9 metros';
            spans[1].textContent = 'médio';
            spans[2].textContent = 'normal';
            spans[3].textContent = 'atributos padrão';
        }
    }

    // Seleciona todas as divs .race e adiciona os event listeners
    document.querySelectorAll('.races-icons .race').forEach(raceDiv => {
        raceDiv.addEventListener('click', () => {
            // Acessa a imagem dentro da div .race
            const img = raceDiv.querySelector('img');
            const raceId = img.id;
            
            // Atualiza a imagem principal
            const fullPath = `/static/imagens/Icons/Races/${raceId}.png`;
            mainRaceImage.src = fullPath;
            
            // Atualiza as características da raça
            atualizarCaracteristicas(raceId);
            
            // Adicionando feedback visual ao clicar
            raceDiv.classList.add('active');
            
            // Removendo a classe 'active' de outras divs
            document.querySelectorAll('.races-icons .race').forEach(otherDiv => {
                if (otherDiv !== raceDiv) {
                    otherDiv.classList.remove('active');
                }
            });
        });
    });

    // Atualiza inicialmente com a primeira raça (opcional)
    const primeiraRace = document.querySelector('.races-icons .race');
    if (primeiraRace) {
        primeiraRace.click();
    }
});