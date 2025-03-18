document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript carregado!");

    const params = new URLSearchParams(window.location.search);
    const modalType = params.get("modal");

    // ✅ Abre o modal correto após recarregar a página
    if (modalType === "register") {
        openModal("registerModal");
    } else if (modalType === "forgot") {
        openModal("forgotPasswordModal");
    } else if (modalType === "login") {
        openModal("loginModal");
    }

    // ✅ Exibe mensagens no modal de login
    const loginMessage = document.getElementById("loginMessage");
    const loginError = localStorage.getItem("loginError");

    if (loginError) {
        loginMessage.innerText = loginError;
        loginMessage.style.display = "block";
        openModal("loginModal");
        localStorage.removeItem("loginError");
    }

    // ✅ Captura erro via URL e redireciona corretamente
    const urlError = params.get("error");
    if (urlError) {
        localStorage.setItem("loginError", urlError);
        window.location.href = "/login/";
    }

    // ✅ Exibe mensagens no modal de cadastro
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

    // ✅ Exibe mensagens armazenadas no LocalStorage para o cadastro
    const storedRegisterError = localStorage.getItem("registerError");
    const storedRegisterSuccess = localStorage.getItem("registerSuccess");
    const keepModalOpen = localStorage.getItem("keepModalOpen");

    if (keepModalOpen === "register" && (storedRegisterError || storedRegisterSuccess)) {
        if (storedRegisterError) {
            registerMessage.innerText = storedRegisterError;
            registerMessage.style.color = "red";
            registerMessage.style.display = "block";
        }
        if (storedRegisterSuccess) {
            registerMessage.innerText = storedRegisterSuccess;
            registerMessage.style.color = "green";
            registerMessage.style.display = "block";
        }
        openModal("registerModal");
    }

    // ✅ Exibe mensagens no modal de reset de senha
    const resetPasswordMessage = document.getElementById("resetPasswordMessage");
    if (resetPasswordMessage) {
        const resetError = params.get("reset_error");
        const resetSuccess = params.get("reset_success");

        if (resetError) {
            resetPasswordMessage.innerText = resetError;
            resetPasswordMessage.style.color = "red";
            resetPasswordMessage.style.display = "block";
        }
        if (resetSuccess) {
            resetPasswordMessage.innerText = resetSuccess;
            resetPasswordMessage.style.color = "green";
            resetPasswordMessage.style.display = "block";
        }
    }

    // ✅ Mantém o modal correto aberto
    if (keepModalOpen === "forgot") {
        openModal("forgotPasswordModal");
    }

    // ✅ Limpa mensagens do LocalStorage após abrir o modal correto
    localStorage.removeItem("registerError");
    localStorage.removeItem("registerSuccess");
    localStorage.removeItem("keepModalOpen");

    // ✅ Esconde mensagens de erro/sucesso após 5 segundos
    setTimeout(() => {
        const messages = document.querySelectorAll("#loginMessage, #registerMessage, #resetPasswordMessage");
        messages.forEach(msg => {
            msg.style.display = "none";
        });
    }, 2500);
});

// 🔥 Função para abrir modal
function openModal(id) {
    document.getElementById(id).style.display = "block";
}

// 🔥 Função para fechar modal
function closeModal(id) {
    document.getElementById(id).style.display = "none";
}

// 🔥 Função para abrir modal de recuperação de senha
function showForgotPassword() {
    closeModal("loginModal");
    openModal("forgotPasswordModal");
}

// 🔥 Fecha modal ao clicar fora dele
window.onclick = function (event) {
    const modals = document.getElementsByClassName("modal");
    for (let modal of modals) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    }
};
