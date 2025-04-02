document.addEventListener("DOMContentLoaded", function () {
    console.log("Preview pronto!");
  
    const input = document.getElementById("image-input");
    const preview = document.getElementById("preview-image");
  
    if (input && preview) {
      input.addEventListener("change", function () {
        const file = input.files[0];
        if (file) {
          console.log("Arquivo selecionado:", file.name);
          const reader = new FileReader();
          reader.onload = function (e) {
            preview.src = e.target.result;
          };
          reader.readAsDataURL(file);
        }
      });
    }
  });
  