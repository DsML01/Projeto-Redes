# Chat com Python - Servidor e Cliente com Sockets

Este projeto foi desenvolvido para a disciplina de Redes de Computadores dos cursos de Ciência e Engenharia da Computação. Ele implementa um sistema de chat em tempo real utilizando **Python**, **Sockets** e **Threads**. Um servidor centraliza as conexões, permitindo que múltiplos clientes troquem mensagens entre si.

## Funcionalidades

- **Servidor**: Gerencia múltiplas conexões de clientes e transmite mensagens de um cliente para todos os outros conectados.
- **Cliente**: Permite que os usuários enviem mensagens para o servidor, que por sua vez distribui essas mensagens para todos os outros clientes conectados.
- **Conexões simultâneas**: Vários clientes podem se conectar ao servidor e enviar mensagens ao mesmo tempo.
- **Desconexões**: O servidor lida com a desconexão de clientes e remove-os da lista de conexões ativas.

## Tecnologias Utilizadas

- **Python 3.x**
- **Sockets** (para comunicação de rede)
- **Threads** (para gerenciar múltiplos clientes simultaneamente)

## Estrutura do Projeto

- `server/`:
  - `server.py`: Código do servidor que gerencia as conexões e transmite as mensagens.
- `cliente.py`: Código do cliente que permite ao usuário interagir com o chat.

## Como Rodar o Projeto

### 1. Instalação do Python

Este projeto é baseado no **Python 3.x**. Caso não tenha o Python instalado, [baixe a versão mais recente aqui](https://www.python.org/downloads/).

### 2. Clone o Repositório

Primeiro, clone o repositório do GitHub:

```bash
git clone https://github.com/DsML01/Projeto-Redes
```

### 3. Execute o Servidor

Para rodar o servidor, abra o terminal, navegue até a pasta server e execute o script server.py:

```bash
cd Projeto-Redes\server
py server.py
```
Isso iniciará o servidor e ele ficará esperando conexões de clientes.

### 4. Execute o Cliente

Em outro terminal, você pode executar o cliente para se conectar ao servidor:

```bash
cd Projeto-Redes\client
py client.py
```
O cliente pedirá que você digite um nome de usuário e, após isso, você poderá começar a enviar mensagens.

### 5. Teste com Vários Clientes
- Abra múltiplos terminais para testar a interação entre os clientes.
- Cada mensagem enviada por um cliente será exibida nos outros clientes conectados.


