document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript carregado!");

    const params = new URLSearchParams(window.location.search);
    const modalType = params.get("modal");

    // Abre o modal correto após recarregar a página
    if (modalType === "register") {
        openModal("registerModal");
    } else if (modalType === "forgot") {
        openModal("forgotPasswordModal");
    } else if (modalType === "login") {
        openModal("loginModal");
    }

    // Mensagens no modal de login
    const loginMessage = document.getElementById("loginMessage");
    const loginError = localStorage.getItem("loginError");
    const keepLoginOpen = localStorage.getItem("keepLoginOpen");

    if (loginError) {
        loginMessage.innerText = loginError;
        loginMessage.classList.add("alert", "error");
        loginMessage.style.display = "block";
    }

    if (keepLoginOpen && loginError) {
        openModal("loginModal");
    }

    // Limpa depois de mostrar
    localStorage.removeItem("loginError");
    localStorage.removeItem("keepLoginOpen");


    // Captura erro via URL
    const urlError = params.get("error");
    if (urlError) {
        localStorage.setItem("loginError", urlError);
        localStorage.setItem("keepLoginOpen", "true");
        window.location.href = "/login/";
    }

    // Mensagens no modal de cadastro
    const registerMessage = document.getElementById("registerMessage");
    const registerError = params.get("register_error");
    const registerSuccess = params.get("register_success");

    if (registerError) {
        const errorMsg = registerError === "senhas-diferentes" ? "As senhas não coincidem." : "Usuário já existe.";
        localStorage.setItem("registerError", errorMsg);
        localStorage.setItem("keepModalOpen", "register");
        window.location.href = "/login/";
    } else if (registerSuccess) {
        localStorage.setItem("registerSuccess", "Cadastro realizado com sucesso!");
        localStorage.setItem("keepModalOpen", "register");
        window.location.href = "/login/";
    }

    const storedRegisterError = localStorage.getItem("registerError");
    const storedRegisterSuccess = localStorage.getItem("registerSuccess");
    const keepModalOpen = localStorage.getItem("keepModalOpen");

    if (keepModalOpen === "register" && registerMessage) {
        if (storedRegisterError) {
            registerMessage.innerText = storedRegisterError;
            registerMessage.className = "message message-error";
            registerMessage.style.display = "block";
        }
        if (storedRegisterSuccess) {
            registerMessage.innerText = storedRegisterSuccess;
            registerMessage.className = "message message-success";
            registerMessage.style.display = "block";
        }
        openModal("registerModal");
    }

    // Mensagens no modal de reset de senha
    const resetPasswordMessage = document.getElementById("resetPasswordMessage");
    if (resetPasswordMessage) {
        const resetError = params.get("reset_error");
        const resetSuccess = params.get("reset_success");

        if (resetError) {
            resetPasswordMessage.innerText = resetError;
            resetPasswordMessage.className = "message message-error";
            resetPasswordMessage.style.display = "block";
        }
        if (resetSuccess) {
            resetPasswordMessage.innerText = resetSuccess;
            resetPasswordMessage.className = "message message-success";
            resetPasswordMessage.style.display = "block";
        }
    }

    if (keepModalOpen === "forgot") {
        openModal("forgotPasswordModal");
    }

    // Limpa dados do localStorage
    localStorage.removeItem("registerError");
    localStorage.removeItem("registerSuccess");
    localStorage.removeItem("keepModalOpen");

    // Esconde mensagens com transição suave
    const allMessages = document.querySelectorAll(".alert");
    allMessages.forEach(msg => {
        setTimeout(() => {
            msg.style.opacity = "0";
            setTimeout(() => {
                msg.style.display = "none";
            }, 500); // tempo da transição
        }, 4000); // tempo visível
    });
});


// 🔥 Abre modal
function openModal(id) {
    document.getElementById(id).style.display = "block";
}

// 🔥 Fecha modal
function closeModal(id) {
    document.getElementById(id).style.display = "none";
}

// 🔥 Troca para modal de esqueci senha
function showForgotPassword() {
    closeModal("loginModal");
    openModal("forgotPasswordModal");
}

// 🔥 Fecha modal ao clicar fora
window.onclick = function (event) {
    const modals = document.getElementsByClassName("modal");
    for (let modal of modals) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    }
};