  // Seleciona todas as imagens de raças
  const raceImages = document.querySelectorAll('.races-icons .race img');
  
  // Imagem principal (melhor usar um ID para precisão)
  const mainRaceImage = document.getElementById('main-race-image');

  // Adiciona evento de clique a cada imagem
  raceImages.forEach(img => {
    img.addEventListener('click', () => {
      mainRaceImage.src = img.src; // Atualiza a imagem principal
      mainRaceImage.alt = img.alt;
    });
});
    // Fechar o dropdown quando clicar fora
    window.addEventListener('click', function(e) {
        if (!e.target.matches('.dropdown-toggle')) {
            if (dropdownMenu) {
                dropdownMenu.style.display = 'none';
            }
        }
    }
);