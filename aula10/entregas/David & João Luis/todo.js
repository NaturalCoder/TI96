// ...existing code...

function addTask(taskName, dueDate) {
    const now = new Date();
    const due = new Date(dueDate);

    if (due <= now) {
        console.error("A data final deve ser no futuro.");
        return;
    }

    const task = {
        name: taskName,
        dueDate: due,
        getTimeRemaining: function () {
            const now = new Date();
            const timeDiff = this.dueDate - now;
            const hours = Math.floor(timeDiff / (1000 * 60 * 60));
            const seconds = Math.floor((timeDiff % (1000 * 60)) / 1000);
            return { hours, seconds };
        }
    };

    tasks.push(task);
    console.log(`Tarefa "${taskName}" adicionada com sucesso!`);
}

// Exemplo de uso:
addTask("Estudar JavaScript", "2023-12-31T23:59:59");

// ...existing code...
function displayTasks() {
    tasks.forEach(task => {
        const { hours, seconds } = task.getTimeRemaining();
        console.log(`Tarefa: ${task.name}, Horas restantes: ${hours}, Segundos restantes: ${seconds}`);
    });
}

// ...existing code...
