document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("image-input");
    const preview = document.getElementById("preview-image");

    if (input && preview) {
        input.addEventListener("change", function () {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();

                reader.onload = function (e) {
                    preview.src = e.target.result;
                };

                reader.readAsDataURL(file);
            }
        });
    }
});
