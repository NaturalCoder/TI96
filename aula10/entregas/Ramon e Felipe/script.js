document.getElementById("fileInput").addEventListener("change", handleImageUpload);

function handleImageUpload(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = new Image();
            img.onload = function() {
                // Exibe a imagem carregada
                document.getElementById("preview").src = e.target.result;
                
                // Chama a função para criar o canvas e converter
                convertToSticker(img);
            };
            img.src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
}

function convertToSticker(image) {
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");

    // Define o tamanho da figurinha do WhatsApp (512x512px)
    const size = 512;
    canvas.width = size;
    canvas.height = size;

    // Desenha a imagem no canvas (ajustando para o tamanho)
    ctx.clearRect(0, 0, size, size); // Limpa o canvas
    ctx.drawImage(image, 0, 0, size, size);

    // Exibe o botão de download
    document.getElementById("downloadBtn").style.display = "inline-block";
    document.getElementById("downloadBtn").onclick = function() {
        // Cria o arquivo .webp para download
        canvas.toBlob(function(blob) {
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = "figurinha.webp";
            link.click();
        }, "image/webp");
    };
}