function adicionarTarefa() {
    const nomeInput = document.getElementById('nomeTarefa');
    const duracaoInput = document.getElementById('duracaoTarefa');
    
    if (!nomeInput.value || !duracaoInput.value) {
        alert('Preencha os campos obrigatórios!');
        return;
    }

    const novaTarefa = {
        id: Date.now(),
        nome: nomeInput.value,
        descricao: document.getElementById('descricaoTarefa').value,
        duracao: parseInt(duracaoInput.value) * 60,
        dataCriacao: Date.now(),
        dataLimite: null,
        progresso: 0,
        expirada: false,
        tempoEsgotado: 0
    };

    novaTarefa.dataLimite = novaTarefa.dataCriacao + (novaTarefa.duracao * 1000);
    tarefas.push(novaTarefa);
    
    nomeInput.value = '';
    document.getElementById('descricaoTarefa').value = '';
    duracaoInput.value = '';
    
    salvarLocalStorage();
    renderizarTarefas(true);
}

function atualizarTempo() {
    const agora = Date.now();
    
    tarefas.forEach(tarefa => {
        const tempoRestante = tarefa.dataLimite - agora;
        tarefa.progresso = ((agora - tarefa.dataCriacao) / (tarefa.dataLimite - tarefa.dataCriacao)) * 100;
        
        if (tempoRestante <= 0) {
            tarefa.expirada = true;
            tarefa.tempoEsgotado = agora - tarefa.dataLimite;
        }
    });
    
    renderizarTarefas();
}

function renderizarTarefas(novaAdicao = false) {
    const container = document.getElementById('listaTarefas');
    container.innerHTML = '';
    
    tarefas.forEach(tarefa => {
        const elemento = document.createElement('div');
        elemento.id = `tarefa-${tarefa.id}`;
        elemento.className = `cartao-tarefa${novaAdicao ? ' nova' : ''}`;
        
        let tempoTexto = tarefa.expirada 
            ? `Tempo Esgotado! ${formatarTempo(tarefa.tempoEsgotado, true)}`
            : formatarTempo(tarefa.dataLimite - Date.now());
        
        elemento.innerHTML = `
            <h3>${tarefa.nome}</h3>
            ${tarefa.descricao ? `<p>${tarefa.descricao}</p>` : ''}
            <div class="barra-progresso">
                <div class="progresso" style="width: ${Math.min(tarefa.progresso, 100)}%"></div>
            </div>
            <div class="contador-tempo">${tempoTexto}</div>
            <button onclick="removerTarefa(${tarefa.id})">🗑️ Remover</button>
        `;
        
        if (tarefa.expirada) {
            elemento.classList.add('expirada');
        }
        
        container.appendChild(elemento);
    });
}

function formatarTempo(milissegundos, esgotado = false) {
    if (milissegundos <= 0 && !esgotado) return 'Tempo Esgotado!';
    
    const segundos = Math.floor(milissegundos / 1000);
    const minutos = Math.floor(segundos / 60);
    const horas = Math.floor(minutos / 60);
    const minutosRestantes = minutos % 60;
    const segundosRestantes = segundos % 60;
    
    if (horas > 0) {
        return `${horas}h ${minutosRestantes}: ${segundosRestantes}`;
    } else {
        return `${minutosRestantes}m ${segundosRestantes}s`;
    }
}

function removerTarefa(id) {
    const elemento = document.getElementById(`tarefa-${id}`);
    if (elemento) {
        elemento.style.opacity = '0';
        elemento.style.transform = 'translateY(-1rem)';
        setTimeout(() => elemento.remove(), 300);
    }
    tarefas = tarefas.filter(tarefa => tarefa.id !== id);
    salvarLocalStorage();
}

function salvarLocalStorage() {
    localStorage.setItem('tarefas', JSON.stringify(tarefas));
}

setInterval(atualizarTempo, 1000);
renderizarTarefas();
