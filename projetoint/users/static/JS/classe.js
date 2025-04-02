
// Caminho base das imagens processado pelo Django
const STATIC_BASE = "{% static 'imagens/Classes/' %}";

document.addEventListener('DOMContentLoaded', () => {
    const mainRaceImage = document.getElementById('main-class-image');
    const mainRaceImage1 = document.getElementById('main-class-image1');
    const mainRaceImage2 = document.getElementById('main-class-image2');
    const mainRaceImage3 = document.getElementById('main-class-image3');
    const mainRaceImage4 = document.getElementById('main-class-image4');

    

    document.querySelectorAll('.classe-icons img').forEach(img => {
        img.addEventListener('click', () => {
            const classId = img.id;
            const fileName = classId;
            const fullPath = `/static/imagens/Classes/${fileName}.png`;
            const fullPath1 = `/static/imagens/Classes/${fileName}1.png`;
            const fullPath2 = `/static/imagens/Classes/${fileName}2.png`;
            const fullPath3 = `/static/imagens/Classes/${fileName}3.png`;
            const fullPath4 = `/static/imagens/Classes/${fileName}4.png`;



            
                        
            console.log('Caminho real:', fullPath);
            console.log('Caminho real:', fullPath1);
            console.log('Caminho real:', fullPath2);
            console.log('Caminho real:', fullPath3);
            console.log('Caminho real:', fullPath4);


            mainRaceImage.src = fullPath;
            mainRaceImage1.src = fullPath1;
            mainRaceImage2.src = fullPath2;
            mainRaceImage3.src = fullPath3;
            mainRaceImage4.src = fullPath4;

        });
    });


});




