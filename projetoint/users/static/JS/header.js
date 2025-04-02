    // Fechar o dropdown quando clicar fora
    function handleClickOutside(e) {
        if (!e.target.matches('.dropdown-toggle')) {
            const dropdownMenu = document.querySelector('.dropdown-menu');
            if (dropdownMenu) {
                dropdownMenu.style.display = 'none';
                // Opcional: remover o listener após o uso
                window.removeEventListener('click', handleClickOutside);
            }
        }
    }
    
    // Quando abrir o dropdown:
    window.addEventListener('click', handleClickOutside);