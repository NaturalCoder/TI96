let saldo = 0;
let modoInfinito = false;
const symbols = ['🍒', '🍋', '🍇', '🔔', '💎'];

function setDinheiro() {
    let valor = parseInt(document.getElementById('valorInicial').value);
    if (!isNaN(valor) && valor > 0) {
        saldo = valor;
        iniciarJogo();
    } else {
        alert('Digite um valor válido!');
    }
}


function modoTeste() {
    modoInfinito = true;
    saldo = Infinity;
    atualizarSaldo();
}

function iniciarJogo() {
    document.getElementById('setup-screen').style.display = 'none';
    document.getElementById('game-screen').style.display = 'block';
    atualizarSaldo();
}

function atualizarSaldo() {
    document.getElementById('saldo').textContent = modoInfinito ? '∞' : saldo;
}

function adicionarDinheiro() {
    let valor = parseInt(document.getElementById('valorAdicionar').value);
    if (!isNaN(valor) && valor > 0) {
        saldo += valor;
        atualizarSaldo();
    } else {
        alert('Digite um valor válido!');
    }
}

function spinReels() {
    if (!modoInfinito && saldo < 10) {
        alert('Saldo insuficiente!');
        return;
    }

    if (!modoInfinito) saldo -= 10;
    atualizarSaldo();

    let slots = [
        document.getElementById('slot1'),
        document.getElementById('slot2'),
        document.getElementById('slot3')
    ];

    let results = [];
    let spinTime = setInterval(() => {
        slots.forEach((slot, index) => {
            let randomSymbol = symbols[Math.floor(Math.random() * symbols.length)];
            slot.textContent = randomSymbol;
            results[index] = randomSymbol;
        });
    }, 100);

    setTimeout(() => {
        clearInterval(spinTime);
        checkWin(results);
    }, 2000);
}

function checkWin(results) {
    let message = document.getElementById('message');
    if (results[0] === results[1] && results[1] === results[2]) {
        saldo += 100;
        message.textContent = '🎉 JACKPOT! Você ganhou R$100! 🎉';
    } else if (results[0] === results[1] || results[1] === results[2] || results[0] === results[2]) {
        saldo += 20;
        message.textContent = '💰 Você ganhou R$20! 💰';
    } else {
        message.textContent = '😢 Tente novamente!';
    }
    atualizarSaldo();
}


function abrirPopup() {
    document.getElementById("popup").style.display = "flex";
}

function fecharPopup() {
    document.getElementById("popup").style.display = "none";
}

document.addEventListener("DOMContentLoaded", function() {
    const addMoneyBtn = document.getElementById("add-money-btn");
    const popupAddMoney = document.getElementById("popup-add-money");
    const closePopupBtn = document.getElementById("close-popup");
    const confirmAddMoneyBtn = document.getElementById("confirm-add-money");
    const moneyInput = document.getElementById("valornovo");
    let balance = 1000; // Exemplo de saldo inicial

    // Exibir o popup ao clicar no botão
    addMoneyBtn.addEventListener("click", function() {
        popupAddMoney.style.display = "block";
    });

    // Fechar o popup
    closePopupBtn.addEventListener("click", function() {
        popupAddMoney.style.display = "none";
    });

    // Adicionar dinheiro ao saldo
    confirmAddMoneyBtn.addEventListener("click", function() {
        const amount = parseFloat(valornovo.value);
        if (!isNaN(amount) && amount > 0) {
            balance += amount;
            popupAddMoney.style.display = "none";
            saldo += amount // Fechar popup
        } else {
            alert("Digite um valor válido!");
        }
        atualizarSaldo();
    });
});