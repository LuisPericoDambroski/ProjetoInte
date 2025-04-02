document.addEventListener('DOMContentLoaded', function() {
    const addCharacterBtn = document.getElementById('addCharacterBtn');
    const newCharacterForm = document.getElementById('newCharacterForm');
    const cancelFormBtn = document.getElementById('cancelFormBtn');
    const saveCharacterBtn = document.getElementById('saveCharacterBtn');
    const characterSheets = document.querySelector('.character-sheets');
    
    // Mostrar formulário ao clicar no botão
    addCharacterBtn.addEventListener('click', function() {
        newCharacterForm.style.display = 'block';
        addCharacterBtn.style.display = 'none';
    });
    
    // Esconder formulário ao cancelar
    cancelFormBtn.addEventListener('click', function() {
        newCharacterForm.style.display = 'none';
        addCharacterBtn.style.display = 'block';
    });
    
    // Adicionar nova ficha
    saveCharacterBtn.addEventListener('click', function() {
        const name = document.getElementById('characterName').value;
        const level = document.getElementById('characterLevel').value;
        const charClass = document.getElementById('characterClass').value;
        const origin = document.getElementById('characterOrigin').value;
        const deity = document.getElementById('characterDeity').value;
        const race = document.getElementById('characterRace').value;
        
        if (name && level && charClass) {
            const newCard = document.createElement('div');
            newCard.className = 'character-card';
            newCard.innerHTML = `
                <h2>${name}</h2>
                <p><strong>Level:</strong> ${level}</p>
                <p><strong>Classe:</strong> ${charClass}</p>
                <p><strong>Origem:</strong> ${origin}</p>
                <p><strong>Deus:</strong> ${deity}</p>
                <p><strong>Raça:</strong> ${race}</p>
            `;
            
            characterSheets.appendChild(newCard);
            
            // Resetar formulário
            document.getElementById('characterName').value = '';
            document.getElementById('characterLevel').value = '';
            document.getElementById('characterClass').value = '';
            document.getElementById('characterOrigin').value = '';
            document.getElementById('characterDeity').value = '';
            document.getElementById('characterRace').value = '';
            
            newCharacterForm.style.display = 'none';
            addCharacterBtn.style.display = 'block';
        } else {
            alert('Por favor, preencha pelo menos Nome, Level e Classe!');
        }
    });
});