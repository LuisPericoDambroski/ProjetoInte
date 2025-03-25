document.addEventListener("DOMContentLoaded", function () {
    const raceElements = document.querySelectorAll(".race");
    const raceIcon = document.querySelector(".race-description .Icon img");
    const raceTitle = document.querySelector(".race-description .description h3");
    const raceText = document.querySelector(".race-description .description p");

    // Informações das raças
    const raceInfo = {
        "Anão": {
            img: '../imagens/Icons/Races/Anão 512px.png',
            text: "Os anões são conhecidos por sua resistência e habilidade em metalurgia e mineração."
        },
        "Dhallan": {
            img: "/projetoint/projetoint/templetes/imagens/Imagens/Icons/Races/Dhallan 512px.png",
            text: "Dhallans possuem uma forte conexão com a natureza e a magia elemental."
        },
        "Elfo": {
            img: "/projetoint/projetoint/templetes/imagens/Imagens/Icons/Races/Elfo 512px.png",
            text: "Elfos são ágeis e sábios, conhecidos por sua longevidade e habilidades arcanas."
        },
        "Goblin": {
            img: "/projetoint/projetoint/templetes/imagens/Imagens/Icons/Races/Goblin 512px.png",
            text: "Goblins são astutos e rápidos, geralmente sobrevivendo através da engenhosidade."
        },
        "Golem": {
            img: "/projetoint/projetoint/templetes/imagens/Imagens/Icons/Races/Golem 512px.png",
            text: "Golems são seres artificiais animados por magia, resistentes e fortes."
        },
        "Humano": {
            img: "/projetoint/projetoint/templetes/imagens/Imagens/Icons/Races/Humano 512px.png",
            text: "Os humanos são versáteis e adaptáveis, podendo se destacar em qualquer área."
        },
        "Hynne": {
            img: "/projetoint/projetoint/templetes/imagens/Imagens/Icons/Races/Hynne 512px.png",
            text: "Hynnes são pequenos e ágeis, conhecidos por sua esperteza e habilidades sociais."
        },
        "Kliren": {
            img: "/projetoint/projetoint/templetes/imagens/Imagens/Icons/Races/Kliren 512px.png",
            text: "Klirens são intelectuais e racionais, sempre em busca de conhecimento."
        },
        "Lefou": {
            img: "/projetoint/projetoint/templetes/imagens/Imagens/Icons/Races/Lefou 512px.png",
            text: "Lefous são mutantes marcados pelo caos, dotados de habilidades únicas."
        },
        "Medusa": {
            img: "/projetoint/projetoint/templetes/imagens/Imagens/Icons/Races/medusa 512px.png",
            text: "Medusas possuem um olhar petrificante e uma beleza exótica e perigosa."
        },
        "Minotauro": {
            img: "/projetoint/projetoint/templetes/imagens/Imagens/Icons/Races/Minotauro 512px.png",
            text: "Minotauros são guerreiros poderosos, conhecidos por sua força e bravura."
        },
        "Osteon": {
            img: "/projetoint/projetoint/templetes/imagens/Imagens/Icons/Races/Osteon 512px.png",
            text: "Osteons são mortos-vivos conscientes que buscam um propósito em sua nova existência."
        },
        "Qareen": {
            img: "/projetoint/projetoint/templetes/imagens/Imagens/Icons/Races/Qareen 512px.png",
            text: "Qareens são seres encantadores, descendentes de gênios e dotados de poderes mágicos."
        },
        "Sílfide": {
            img: "/projetoint/projetoint/templetes/imagens/Imagens/Icons/Races/Sílfide 512px.png",
            text: "Sílfides são etéreas e graciosas, ligadas ao elemento ar e à liberdade."
        },
        "Suraggel": {
            img: "/projetoint/projetoint/templetes/imagens/Imagens/Icons/Races/Suraggel 512px.png",
            text: "Suraggels possuem linhagens divinas e demoníacas, divididos entre luz e trevas."
        },
        "Tritão": {
            img: "/projetoint/projetoint/templetes/imagens/Imagens/Icons/Races/Tritão 512px.png",
            text: "Tritões são habitantes dos oceanos, ágeis nadadores e dotados de grande resistência."
        },
        "Trog": {
            img: "/projetoint/projetoint/templetes/imagens/Imagens/Icons/Races/Trog 512px.png",
            text: "Trogs são reptilianos resistentes, adaptados a ambientes inóspitos e perigosos."
        }
    };

    raceElements.forEach(race => {
            race.addEventListener("click", function () {
                const imgElement = this.querySelector("img"); // Obtém a imagem dentro do .race
                const raceName = imgElement.id; // Pega o id da imagem
    
                if (raceInfo[raceName]) {
                    raceIcon.src = raceInfo[raceName].img;
                    raceTitle.textContent = raceName;
                    raceText.textContent = raceInfo[raceName].text;
                }
            });
        });
});

document.addEventListener('DOMContentLoaded', function() {
    const dropdownToggle = document.getElementById('dropdownMenuButton');
    const dropdownMenu = document.querySelector('.dropdown-menu');
    
    if (dropdownToggle) {
        dropdownToggle.addEventListener('click', function(e) {
            e.preventDefault();
            dropdownMenu.style.display = dropdownMenu.style.display === 'block' ? 'none' : 'block';
        });
    }
    
    // Fechar o dropdown quando clicar fora
    window.addEventListener('click', function(e) {
        if (!e.target.matches('.dropdown-toggle')) {
            if (dropdownMenu) {
                dropdownMenu.style.display = 'none';
            }
        }
    });
});