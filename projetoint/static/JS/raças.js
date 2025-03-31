
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
