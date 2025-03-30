
// Caminho base das imagens processado pelo Django
const STATIC_BASE = "{% static 'imagens/Classes/' %}";

document.addEventListener('DOMContentLoaded', () => {
    const mainRaceImage = document.getElementById('main-class-image');
    

    document.querySelectorAll('.classe-icons img').forEach(img => {
        img.addEventListener('click', () => {
            const classId = img.id;
            const fileName = classId;
            const fullPath = `/static/imagens/Classes/${fileName}.png`;
                        
            console.log('Caminho real:', fullPath);
            mainRaceImage.src = fullPath;
        });
    });
});