document.addEventListener('DOMContentLoaded', function() {
    const receitaForm = document.getElementById('receitaForm');
    const ingredienteInput = document.getElementById('ingredienteInput');
    const ingredientesList = document.getElementById('ingredientesList');

    if (receitaForm) {
        receitaForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const nome = document.getElementById('nomeInput').value;
            const modoPreparo = document.getElementById('modoPreparoInput').value;

            if (!nome || !modoPreparo) {
                alert('Por favor, preencha todos os campos.');
                return;
            }

            alert('Receita cadastrada com sucesso!');
            receitaForm.reset();
            ingredientesList.innerHTML = '';
        });
    }

    if (ingredienteInput) {
        ingredienteInput.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                event.preventDefault();
                const ingrediente = ingredienteInput.value.trim();
                if (ingrediente) {
                    const li = document.createElement('li');
                    li.textContent = ingrediente;
                    ingredientesList.appendChild(li);
                    ingredienteInput.value = '';
                }
            }
        });
    }
});