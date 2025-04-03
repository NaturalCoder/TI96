document.getElementById("fileInput").addEventListener("change", handleImageUpload);

function handleImageUpload(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = new Image();
            img.onload = function() {
                document.getElementById("preview").src = e.target.result;
                
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

    const size = 512;
    canvas.width = size;
    canvas.height = size;

    ctx.clearRect(0, 0, size, size); // Limpa o canvas
    ctx.drawImage(image, 0, 0, size, size);

    
    document.getElementById("downloadBtn").style.display = "inline-block";
    document.getElementById("downloadBtn").onclick = function() {
        canvas.toBlob(function(blob) {
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = "figurinha.webp";
            link.click();
        }, "image/webp");
    };
}