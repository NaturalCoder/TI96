let tarefas = [];
let contador = 0;

document.getElementById('adicionarTarefaBtn').addEventListener('click', () => {
    const novaTarefaInput = document.getElementById('novaTarefa');
    const dataFinalInput = document.getElementById('dataFinal');
    const listaTarefas = document.getElementById('listaTarefas');
    const contadorTarefas = document.getElementById('contadorTarefas');

    const tarefaTexto = novaTarefaInput.value.trim();
    const dataFinal = new Date(dataFinalInput.value);

    if (!tarefaTexto || isNaN(dataFinal.getTime())) {
        alert('Por favor, insira uma tarefa válida e uma data/hora final.');
        return;
    }

    const tarefaDiv = document.createElement('div');
    tarefaDiv.classList.add('tarefa');

    const tarefaDescricao = document.createElement('p');
    tarefaDescricao.textContent = tarefaTexto;
    tarefaDescricao.style.margin = '0'; // Adiciona espaçamento consistente
    tarefaDescricao.style.padding = '5px 0'; // Ajusta o espaçamento interno

    const tempoRestante = document.createElement('span');
    tempoRestante.classList.add('tempo-restante');

    const atualizarTempoRestante = () => {
        const agora = new Date();
        const diferenca = dataFinal - agora;

        if (diferenca <= 0) {
            tempoRestante.textContent = 'Tempo esgotado';
            clearInterval(intervalo);
        } else {
            const horas = Math.floor(diferenca / (1000 * 60 * 60));
            const minutos = Math.floor((diferenca % (1000 * 60 * 60)) / (1000 * 60));
            const segundos = Math.floor((diferenca % (1000 * 60)) / 1000);
            tempoRestante.textContent = `Restam ${horas}h ${minutos}m ${segundos}s`;
        }
    };

    const intervalo = setInterval(atualizarTempoRestante, 1000);
    atualizarTempoRestante();

    tarefaDiv.appendChild(tarefaDescricao);
    tarefaDiv.appendChild(tempoRestante);
    listaTarefas.appendChild(tarefaDiv);

    novaTarefaInput.value = '';
    dataFinalInput.value = '';

    contadorTarefas.textContent = listaTarefas.children.length;
});

function removerTarefa(button) {
    const tarefaItem = button.parentElement;
    tarefaItem.remove();
    atualizarContador();
}

function atualizarContador() {
    const contadorTarefas = document.getElementById('contadorTarefas');
    const totalTarefas = document.querySelectorAll('.tarefa-item').length;
    contadorTarefas.textContent = totalTarefas;
}

function atualizarLista() {
    const lista = document.getElementById('listaTarefas');
    lista.innerHTML = '';

    tarefas.forEach(tarefa => {
        const div = document.createElement('div');
        div.className = `tarefa ${tarefa.status}`;

        div.innerHTML = `
            <input type="checkbox" 
                   ${tarefa.status === 'concluida' ? 'checked' : ''} 
                   onchange="alterarStatus(${tarefa.id})">
            <span>${tarefa.texto}</span>
        `;

        lista.appendChild(div);
    });
}

function alterarStatus(id) {
    const tarefa = tarefas.find(t => t.id === id);
    if (tarefa) {
        tarefa.status = tarefa.status === 'pendente' ? 'concluida' : 'pendente';
        atualizarLista();
        atualizarTarefa(tarefa);
    }
}

// Funções para comunicação com o backend
async function salvarTarefa(tarefa) {
    try {
        await fetch('http://localhost:5000/tarefas', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(tarefa)
        });
    } catch (erro) {
        console.error('Erro ao salvar tarefa:', erro);
    }
}

async function atualizarTarefa(tarefa) {
    try {
        await fetch(`http://localhost:5000/tarefas/${tarefa.id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(tarefa)
        });
    } catch (erro) {
        console.error('Erro ao atualizar tarefa:', erro);
    }
}

function adicionarTarefa() {
    const novaTarefaInput = document.getElementById('novaTarefa');
    const listaTarefas = document.getElementById('listaTarefas');
    const tarefaTexto = novaTarefaInput.value;

    if (tarefaTexto.trim() === '') return;

    const tarefaDiv = document.createElement('div');
    tarefaDiv.classList.add('tarefa');

    const tarefaSpan = document.createElement('span');
    tarefaSpan.textContent = tarefaTexto;

    // Ícone de andamento
    const andamentoIcone = document.createElement('img');
    andamentoIcone.src = 'andamento.png'; // Substitua pelo caminho correto do ícone
    andamentoIcone.alt = 'Em andamento';
    andamentoIcone.title = 'Em andamento';
    andamentoIcone.classList.add('icone-tarefa');
    andamentoIcone.addEventListener('click', () => alterarStatusTarefa(tarefaDiv, 'andamento'));

    // Ícone de concluído
    const concluidoIcone = document.createElement('img');
    concluidoIcone.src = 'concluido.png'; // Substitua pelo caminho correto do ícone
    concluidoIcone.alt = 'Concluído';
    concluidoIcone.title = 'Concluído';
    concluidoIcone.classList.add('icone-tarefa');
    concluidoIcone.addEventListener('click', () => alterarStatusTarefa(tarefaDiv, 'concluido'));

    // Ícone de não concluído
    const naoConcluidoIcone = document.createElement('img');
    naoConcluidoIcone.src = 'nao-concluido.png'; // Substitua pelo caminho correto do ícone
    naoConcluidoIcone.alt = 'Não concluído';
    naoConcluidoIcone.title = 'Não concluído';
    naoConcluidoIcone.classList.add('icone-tarefa');
    naoConcluidoIcone.addEventListener('click', () => alterarStatusTarefa(tarefaDiv, 'nao-concluido'));

    tarefaDiv.appendChild(tarefaSpan);
    tarefaDiv.appendChild(andamentoIcone);
    tarefaDiv.appendChild(concluidoIcone);
    tarefaDiv.appendChild(naoConcluidoIcone);
    listaTarefas.appendChild(tarefaDiv);

    novaTarefaInput.value = '';
    atualizarContador();
}

function alterarStatusTarefa(tarefaDiv, status) {
    if (status === 'andamento') {
        tarefaDiv.style.textDecoration = 'none';
    } else if (status === 'concluido') {
        tarefaDiv.style.textDecoration = 'line-through';
    } else if (status === 'nao-concluido') {
        tarefaDiv.style.textDecoration = 'none';
        exibirNotificacao(tarefaDiv);
    }
}

document.getElementById('listaTarefas').addEventListener('click', (event) => {
    if (event.target.classList.contains('icone')) {
        const tarefaDiv = event.target.closest('.tarefa');
        if (event.target.title === 'Concluída') {
            tarefaDiv.style.textDecoration = 'line-through';
        } else if (event.target.title === 'Não Concluída') {
            exibirNotificacao(tarefaDiv);
        }
    }
});

function exibirNotificacao(tarefaDiv) {
    const notificacao = document.getElementById('notificacao');
    notificacao.style.display = 'block';

    document.getElementById('remarcarSim').onclick = () => {
        const novaData = prompt('Digite a nova data e hora (AAAA-MM-DDTHH:mm):');
        if (novaData) {
            tarefaDiv.querySelector('span').textContent += ` - Remarcada para ${new Date(novaData).toLocaleString()}`;
        }
        notificacao.style.display = 'none';
    };

    document.getElementById('remarcarNao').onclick = () => {
        notificacao.style.display = 'none';
    };
}
