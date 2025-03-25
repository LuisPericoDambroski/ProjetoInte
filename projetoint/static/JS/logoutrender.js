async function handleLogout(event) {
    event.preventDefault();
    
    try {
        const response = await fetch("{% url 'logout' %}", {
            method: 'POST',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': getCSRFToken(),
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            credentials: 'include',
            body: new URLSearchParams({})  // Corpo vazio mas necessário para POST
        });

        if (response.ok) {
            // Força um hard refresh para limpar qualquer cache
            window.location.href = window.location.href + '?logout=' + Date.now();
        } else {
            console.error('Logout falhou');
            window.location.reload();
        }
    } catch (error) {
        console.error('Erro durante logout:', error);
        window.location.href = "{% url 'home' %}";
    }
}

function getCSRFToken() {
    const csrfInput = document.querySelector('[name=csrfmiddlewaretoken]');
    return csrfInput ? csrfInput.value : null;
}

// Adiciona event listener melhorado
function setupLogout() {
    document.querySelectorAll('.logout-link').forEach(link => {
        link.addEventListener('click', handleLogout);
        link.addEventListener('auxclick', handleLogout);  // Para clique com botão do meio
    });
}

// Executa quando o DOM estiver pronto
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupLogout);
} else {
    setupLogout();
}