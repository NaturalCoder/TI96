document.getElementById('abrir-cadastro').addEventListener('click', function() {
    document.getElementById('cadastro').style.display = 'block';
  });
  
  document.getElementById('fechar-modal').addEventListener('click', function() {
    document.getElementById('cadastro').style.display = 'none';
  });
  
  // Lógica para cadastro de filmes
  document.getElementById('form-cadastro').addEventListener('submit', function(e) {
    e.preventDefault();
  
    const nome = document.getElementById('nome').value;
    const imagem = document.getElementById('imagem').value;
    const descricao = document.getElementById('descricao').value;
    const link = document.getElementById('link').value;
  
    // Aqui você pode fazer uma requisição AJAX para salvar os dados no backend (se necessário)
    alert(`Filme ${nome} cadastrado com sucesso!`);
  
    // Limpar o formulário após o envio
    document.getElementById('form-cadastro').reset();
    document.getElementById('cadastro').style.display = 'none';
  });

  const express = require('express');
const app = express();
const fs = require('fs');
const path = require('path');

app.use(express.json());
app.use(express.static('public')); // Para servir arquivos estáticos como HTML, CSS, JS

const filmesFile = path.join(__dirname, 'filmes.json');

// Endpoint para obter os filmes
app.get('/filmes', (req, res) => {
  fs.readFile(filmesFile, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).send('Erro ao ler filmes');
    }
    res.json(JSON.parse(data));
  });
});

// Endpoint para cadastrar um novo filme
app.post('/filmes', (req, res) => {
  const { nome, imagem, descricao, link } = req.body;
  const novoFilme = { nome, imagem, descricao, link };

  fs.readFile(filmesFile, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).send('Erro ao ler filmes');
    }
    const filmes = JSON.parse(data);
    filmes.push(novoFilme);

    fs.writeFile(filmesFile, JSON.stringify(filmes, null, 2), (err) => {
      if (err) {
        return res.status(500).send('Erro ao salvar filme');
      }
      res.status(200).send('Filme cadastrado com sucesso');
    });
  });
});

app.listen(3000, () => {
  console.log('Servidor rodando na porta 3000');
});

[
    {
      "nome": "Filme 1",
      "imagem": "imagem-filme1.jpg",
      "descricao": "Descrição do Filme 1",
      "link": "https://www.youtube.com/watch?v=ID_DO_VIDEO"
    }
  ]