# 🚚 API de Deliveries

Esta API foi desenvolvida para gerenciar pedidos de delivery, oferecendo funcionalidades robustas e escaláveis para cadastro, atualização, consulta e exclusão de pedidos. Utilizando **Python** com o framework **Flask** e o banco de dados **MongoDB**, a API foi projetada para atender a sistemas de delivery modernos e dinâmicos. Além disso, ela integra validação de dados com **Cerberus**, garante a qualidade do código com **pylint**, e proporciona testes automatizados com **pytest**, tornando o desenvolvimento mais seguro e eficiente.

## 🛠️ Tecnologias Utilizadas

- 🐍 Python - Linguagem de programação principal utilizada no desenvolvimento da API.
- 🌐 Flask - Framework web utilizado para a criação da API RESTful.
- 🍃 MongoDB - Banco de dados NoSQL utilizado para armazenar os pedidos.
- 🔍 Cerberus - Biblioteca para validação de dados de entrada nas requisições.
- 📏 pylint - Ferramenta de análise estática para garantir a qualidade do código Python.
- 📦 pymongo - Biblioteca que permite a comunicação entre Python e MongoDB.
- 🧪 pytest - Framework de testes utilizado para garantir a confiabilidade do código.
- 🔑 python-dotenv - Biblioteca para gerenciar variáveis de ambiente de forma segura.

## ⚙️ Funcionalidades

- 📝 Criar pedido - Permite cadastrar um novo pedido no sistema.
- 🔍 Buscar pedido - Retorna as informações de um pedido específico com base no ID.
- 🔄 Atualizar pedido - Atualiza os detalhes de um pedido existente.
- ❌ Deletar pedido - Remove um pedido do banco de dados.
- 📜 Listar pedidos - Retorna uma lista com todos os pedidos cadastrados.

## 🚀 Como Executar o Projeto

### 📋 Pré-requisitos

Certifique-se de ter instalado:

- ✅ Python 3+
- ✅ [MongoDBCompass](https://www.mongodb.com/try/download/compass)

### 📦 Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/joschonarth/flask-delivery-api.git
   cd seu-repositorio
   ```

2. Crie e ative um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

### 🗄️ Configuração do MongoDB

Certifique-se de que o MongoDB esteja em execução e configure a URL de conexão no arquivo `.env`:

```bash
MONGO_USER=admin
MONGO_PASSWORD=password
MONGO_HOST=localhost
MONGO_PORT=27017
MONGO_DATABASE=delivery_db
```

### ▶️ Executando a API

```bash
python run.py
```

## 🔗 Endpoints

### 📝 Criar Pedido

- Método: `POST`
- Rota: `/delivery/order`
- Corpo da Requisição:

    ```json
    {
        "data": {
            "order_id": 1,
            "customer": "John Doe",
            "items": [
                {"name": "Laptop", "quantity": 1},
                {"name": "Keyboard", "quantity": 1}
            ],
            "total": 900.00,
            "shipped": true
        }
    }
    ```

### 🔍 Buscar Pedido

- Método: `GET`
- Rota: `/delivery/order/:order_id`
- Path Variables: `order_id`

### 🔄 Atualizar Pedido

- Método: `PATCH`
- Rota: `/delivery/order/:order_id`
- Path Variables: `order_id`
- Corpo da Requisição:

    ```json
    {
        "data": {
            "items": [
                { "name": "Laptop", "quantity": 2 }
            ]
        }
    }
    ```

### ❌ Deletar Pedido

- Método: `DELETE`
- Rota: `/delivery/order/:order_id`
- Path Variables: `order_id`

### 📜 Listar Pedidos

- Método: `DELETE`
- Rota: `/delivery/orders`

## 🧪 Testes

A API inclui um conjunto de testes automatizados para garantir a confiabilidade das funcionalidades. Os testes são realizados utilizando o framework **pytest**. Eles cobrem operações críticas como a criação, atualização, exclusão e busca de pedidos.

### Executando os Testes

Para rodar os testes, siga os seguintes passos:

1. Certifique-se de que o ambiente virtual esteja ativado e que todas as dependências estejam instaladas.

2. Execute o comando abaixo para rodar todos os testes:

    ```bash
    pytest
    ```

3. Execute os testes com cobertura detalhada, usando o comando abaixo:

    ```bash
    pytest -s -v
    ```

## 🤝 Contribuição

Sinta-se à vontade para contribuir! Fique à vontade para abrir issues e pull requests.
