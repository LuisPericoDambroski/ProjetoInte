// function showTab(tab) {
//     document.querySelectorAll('.form').forEach(form => form.classList.remove('active'));
//     document.getElementById(tab).classList.add('active');
// }

// // Simulação de banco de dados com localStorage
// const users = JSON.parse(localStorage.getItem('users')) || [];

// document.getElementById('cadastro').addEventListener('submit', function(e) {
//     e.preventDefault();
    
//     const user = document.getElementById('cadastro-user').value;
//     const email = document.getElementById('cadastro-email').value;
//     const password = document.getElementById('cadastro-password').value;
    
//     if (users.some(u => u.email === email)) {
//         alert('Email já cadastrado!');
//         return;
//     }

//     users.push({ user, email, password });
//     localStorage.setItem('users', JSON.stringify(users));
//     alert('Cadastro realizado com sucesso!');
//     showTab('login');
// });

// document.getElementById('login').addEventListener('submit', function(e) {
//     e.preventDefault();
    
//     const email = document.getElementById('login-email').value;
//     const password = document.getElementById('login-password').value;
    
//     const user = users.find(u => u.email === email && u.password === password);
    
//     if (user) {
//         alert(`Bem-vindo, ${user.user}!`);
//     } else {
//         alert('Email ou senha incorretos!');
//     }
// });

// document.getElementById('recuperar').addEventListener('submit', function(e) {
//     e.preventDefault();
    
//     const email = document.getElementById('recuperar-email').value;
//     const user = users.find(u => u.email === email);
    
//     if (user) {
//         alert(`Sua senha é: ${user.password}`);
//     } else {
//         alert('Email não cadastrado!');
//     }
// });

// Função para exibir o formulário correspondente
function showTab(tabName) {
    // Oculta todos os formulários
    document.getElementById('login').style.display = 'none';
    document.getElementById('cadastro').style.display = 'none';
    document.getElementById('recuperar').style.display = 'none';
    
    // Exibe o formulário correspondente
    if (tabName === 'login') {
        document.getElementById('login').style.display = 'block';
    } else if (tabName === 'cadastro') {
        document.getElementById('cadastro').style.display = 'block';
    } else if (tabName === 'recuperar') {
        document.getElementById('recuperar').style.display = 'block';
    }
}

// Inicializa com o formulário de login
showTab('login');



// Função para abrir o modal
function openRegisterModal() {
    document.getElementById('registerModal').style.display = 'block';
}

// Função para fechar o modal
function closeRegisterModal() {
    document.getElementById('registerModal').style.display = 'none';
}

// Fechar o modal se clicar fora dele
window.onclick = function(event) {
    if (event.target === document.getElementById('registerModal')) {
        closeRegisterModal();
    }
}
