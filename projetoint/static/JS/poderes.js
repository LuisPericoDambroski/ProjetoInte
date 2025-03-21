function exibirPoder() {
    const seletor = document.getElementById('listaPoderes');
    const exibicao = document.getElementById('poderExibicao');
    const poderSelecionado = seletor.value;

    if (poderSelecionado) {
        exibicao.innerHTML = `
            <h3>${poderSelecionado}</h3>
            <p>${obterDescricaoPoder(poderSelecionado)}</p>
        `;
    } else {
        exibicao.innerHTML = '';
    }
}

function obterDescricaoPoder(poder) {
    const descricoes = {
        'Super Força': 'Capacidade de levantar objetos extremamente pesados e quebrar barreiras físicas.',
        'Invisibilidade': 'Habilidade de se tornar invisível a olho nu sempre que desejar.',
        'Teletransporte': 'Poder para se transportar instantaneamente para qualquer local em segundos.',
        'Visão de Raio-X': 'Capacidade de ver através de paredes e outros objetos sólidos.',
        'Velocidade Sobre-Humana': 'Correr e se mover em velocidades muito além dos limites humanos normais.'
    };

    return descricoes[poder] || 'Descrição não disponível.';
}

/*Atributo*/

function calcularModificador(valor) {
    valor = parseInt(valor);
    if (isNaN(valor)) return 0; // Retorna 0 se não for número
    
    if (valor === 1) return -5;
    if (valor <= 3) return -4;
    if (valor <= 5) return -3;
    if (valor <= 7) return -2;
    if (valor <= 9) return -1;
    if (valor <= 11) return 0;
    
    const modificadores = {
        12: 1, 13: 1,
        14: 2, 15: 2,
        16: 3, 17: 3,
        18: 4, 19: 4,
        20: 5, 21: 5,
        22: 6, 23: 6,
        24: 7, 25: 7
    };
    
    return modificadores[valor] || 0;
}

function atualizarModificador() {
    const span = document.getElementById('valorAtributo');
    const valor = parseInt(span.textContent) || 0; // Usa 0 se inválido
    
    // Mantém o valor entre 1-25
    if (valor < 1) span.textContent = '1';
    if (valor > 25) span.textContent = '25';
    
    const mod = calcularModificador(valor);
    document.getElementById('modificador').textContent = 
        `Modificador: ${mod >= 0 ? '+' : ''}${mod}`;
}

// Eventos
const spanEditavel = document.getElementById('valorAtributo');

// Atualiza quando o usuário termina de editar
spanEditavel.addEventListener('blur', atualizarModificador);

// Valida durante a edição
spanEditavel.addEventListener('input', (e) => {
    // Remove caracteres não numéricos
    e.target.textContent = e.target.textContent.replace(/\D/g, '');
});

// Atualiza inicialmente
atualizarModificador();