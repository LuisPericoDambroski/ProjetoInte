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

function openModal(id) {
    document.getElementById(id).style.display = "block";
}

function closeModal(id) {
    document.getElementById(id).style.display = "none";
}

$("#registerForm").submit(function (event) {
    event.preventDefault();
    $.ajax({
        type: "POST",
        url: "register/",
        data: $(this).serialize(),
        success: function (response) {
            $("#registerMessage").text(response.message).removeClass().addClass(response.status === "success" ? "success-message" : "error-message");
            if (response.status === "success") {
                setTimeout(() => closeModal('registerModal'), 1500);
            }
        },
        error: function () {
            $("#registerMessage").text("Erro ao tentar cadastrar.").removeClass().addClass("error-message");
        }
    });
});

$("#loginForm").submit(function (event) {
    event.preventDefault();
    $.ajax({
        type: "POST",
        url: "login/register/",
        data: $(this).serialize(),
        success: function (response) {
            $("#loginMessage").text(response.message).removeClass().addClass(response.status === "success" ? "success-message" : "error-message");
            if (response.status === "success") {
                setTimeout(() => window.location.href = "/login/", 1500);
            }
        },
        error: function () {
            $("#loginMessage").text("Erro ao tentar logar.").removeClass().addClass("error-message");
        }
    });
});
