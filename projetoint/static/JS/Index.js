
// Caminho base das imagens processado pelo Django
const STATIC_BASE = "{% static 'imagens/Raças/' %}";

document.addEventListener('DOMContentLoaded', () => {
    const mainRaceImage = document.getElementById('main-race-image');
    

    document.querySelectorAll('.races-icons img').forEach(img => {
        img.addEventListener('click', () => {
            const raceId = img.id;
            const fileName = raceId;
            const fullPath = `/static/imagens/Raças/${fileName}.png`;
                        
            console.log('Caminho real:', fullPath);
            mainRaceImage.src = fullPath;
        });
    });
});

console.log(fullPath); // Deve retornar algo como "/static/imagens/Raças/Anao.png"


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