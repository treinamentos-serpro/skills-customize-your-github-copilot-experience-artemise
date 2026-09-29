# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST simples com o framework FastAPI, usando rotas, modelos de dados e respostas em JSON para expor operações básicas de consulta e cadastro.

## 📝 Tarefas

### 🛠️ Configurar a Aplicação FastAPI

#### Descrição
Crie uma aplicação FastAPI mínima e configure o servidor para rodar localmente.

#### Requisitos
O programa concluído deve:

- Importar `FastAPI` e criar uma instância da aplicação.
- Definir uma rota inicial como `GET /` que retorne uma mensagem de boas-vindas.
- Executar a aplicação com um comando Python comum para desenvolvimento.
- Confirmar que a API responde corretamente em um navegador ou cliente HTTP.

### 🛠️ Criar Endpoints de leitura

#### Descrição
Implemente endpoints para listar e buscar itens de uma coleção simples.

#### Requisitos
O programa concluída deve:

- Criar uma rota `GET /items` para retornar uma lista de itens em JSON.
- Criar uma rota `GET /items/{item_id}` para buscar um item específico por identificador.
- Usar dados em memória para simular uma base de dados simples.
- Retornar respostas claras para itens existentes e inexistentes.

### 🛠️ Adicionar Operações de Criação e Atualização

#### Descrição
Expanda a API com endpoints para criar e atualizar recursos.

#### Requisitos
O programa concluído deve:

- Criar uma rota `POST /items` para adicionar um novo item.
- Validar os dados recebidos antes de salvar.
- Criar uma rota `PUT /items/{item_id}` para atualizar um item existente.
- Retornar o item atualizado em formato JSON.
- Demonstrar como a API pode ser consumida por um cliente externo.
