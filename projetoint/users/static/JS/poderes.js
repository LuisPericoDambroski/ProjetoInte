// function carregarPoderes() {
//     const tipoPoder = document.getElementById('tipoPoder').value;
//     const listaPoderes = document.getElementById('listaPoderes');
    
//     if (tipoPoder) {
//         // Limpa as opções atuais
//         listaPoderes.innerHTML = '<option value="">Selecione um poder</option>';
        
//         // Faz uma requisição para obter os poderes do tipo selecionado
//         fetch(`/api/poderes/?tipo=${tipoPoder}`)
//             .then(response => response.json())
//             .then(data => {
//                 data.poderes.forEach(poder => {
//                     const option = document.createElement('option');
//                     option.value = poder.nome;
//                     option.textContent = poder.nome;
//                     listaPoderes.appendChild(option);
//                 });
//                 listaPoderes.disabled = false;
//             });
//     } else {
//         listaPoderes.innerHTML = '<option value="">Selecione um poder</option>';
//         listaPoderes.disabled = true;
//     }
// }

// function exibirPoder() {
//     const seletor = document.getElementById('listaPoderes');
//     const exibicao = document.getElementById('poderExibicao');
//     const poderSelecionado = seletor.value;

//     if (poderSelecionado) {
//         fetch(`/api/poderes/descricao/?nome=${encodeURIComponent(poderSelecionado)}`)
//             .then(response => response.json())
//             .then(data => {
//                 exibicao.innerHTML = `
//                     <h3>${poderSelecionado}</h3>
//                     <p>${data.descricao}</p>
//                 `;
//             });
//     } else {
//         exibicao.innerHTML = '';
//     }
// }

// function salvarPoder() {
//     const tipoPoder = document.getElementById('tipoPoder').value;
//     const poderSelecionado = document.getElementById('listaPoderes').value;
    
//     if (!tipoPoder || !poderSelecionado) {
//         alert('Por favor, selecione um tipo e um poder');
//         return;
//     }
    
//     fetch('/api/poderes/salvar/', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': getCookie('csrftoken'),
//         },
//         body: JSON.stringify({
//             tipo: tipoPoder,
//             nome: poderSelecionado
//         })
//     })
//     .then(response => response.json())
//     .then(data => {
//         if (data.success) {
//             alert('Poder salvo com sucesso!');
//         } else {
//             alert('Erro ao salvar poder: ' + data.error);
//         }
//     });
// }

// // Função auxiliar para obter o token CSRF
// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }

/*Atributo*/

// Função para calcular o modificador
function calcularModificador(valor) {
    return Math.floor((valor - 10) / 2);
}

// Atualizar todos os modificadores
function atualizarModificadores() {
    document.querySelectorAll('.grid-a').forEach(grid => {
        const valorElemento = grid.querySelector('.valor-atributo');
        const modificadorElemento = grid.querySelector('.modificador');
        
        // Converter valor para número e garantir que seja válido
        const valor = parseInt(valorElemento.textContent) || 0; 
        
        // Calcular e exibir modificador
        modificadorElemento.textContent = calcularModificador(valor);
    });
}

// Event listeners para campos editáveis
document.querySelectorAll('.valor-atributo').forEach(elemento => {
    elemento.addEventListener('input', atualizarModificadores);
});

// Calcular modificadores inicialmente
atualizarModificadores();

document.addEventListener('DOMContentLoaded', function() {
    // Mapeamento das raças e suas características
    const racasCaracteristicas = {
        'Sílfide': {
            movimento: '9 metros',
            tamanho: 'Minúsculo',
            visao: 'Penumbra',
            atributos: 'Carisma +2, Destreza +1, Força -2'
        },
        'Humano': {
            movimento: '9 metros',
            tamanho: 'Médio',
            visao: 'Normal',
            atributos: 'Qualquer atributo +2'
        },
        'Elfo': {
            movimento: '9 metros',
            tamanho: 'Médio',
            visao: 'Visão no Escuro',
            atributos: 'Destreza +2, Inteligência +2, Constituição -2'
        },
        // Adicione outras raças aqui...
    };

    // Elementos do DOM
    const inputRaca = document.querySelector('input[name="race"]');
    const caracteristicasDiv = document.querySelector('.caracteristicas');
    const spans = caracteristicasDiv.querySelectorAll('span');

    // Função para atualizar características
    function atualizarCaracteristicas() {
        const racaDigitada = inputRaca.value.trim();
        const caracteristicas = racasCaracteristicas[racaDigitada];

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

    // Ouvinte de eventos para o input
    inputRaca.addEventListener('input', atualizarCaracteristicas);
});