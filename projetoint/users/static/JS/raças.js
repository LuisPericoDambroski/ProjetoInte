document.addEventListener('DOMContentLoaded', () => {
    const mainRaceImage = document.getElementById('main-race-image');

    // Altere o seletor para a div .race (em vez da img)
    document.querySelectorAll('.races-icons .race').forEach(raceDiv => {
        raceDiv.addEventListener('click', () => {
            // Acessa a imagem dentro da div .race
            const img = raceDiv.querySelector('img');
            const raceId = img.id;
            const fullPath = `/static/imagens/Raças/${raceId}.png`;
            
            console.log('Caminho real:', fullPath);
            mainRaceImage.src = fullPath;
        });
    });
});