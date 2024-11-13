import threading
import socket

clients = []

def main():
    
    #AF_INET = IPV4 e SOCK_STREAM = TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Aqui estamos tentando ligar o servidor na porta 1533
    try:
        server.bind(('localhost', 1533))
        server.listen(5) #Se não colocarmos nada, ele aceitará infinitas conexões
        #Porém se colocamos um inteiro como parâmetro, ele aceitará o número de conexões que indicarmos
        print("Servidor iniciado!")
    except:
        print("Não foi possível iniciar o servidor.") 
        return

    while True:
        #Client que é um objeto socket que foi criado no client.py
        #addr é o par ip,porta que representa o endereço e o cliente.
        client, addr = server.accept()
        
        #Adicionando um cliente na lista de clientes
        clients.append(client)
        #print(f"Conexão estabelecida com {addr}")

        #Aqui ele cria uma thread para cada client que se conectar na rede
        #para assim então, tentar receber as mensagens de cada cliente
        #e esperar pela conexão de cada cliente.
        thread = threading.Thread(target=tratamentoDeMensagens, args=[client])
        thread.start()

def tratamentoDeMensagens(client):
    while True:
        try:
            #Cada vez que o cliente enviar uma mensagem, a gente recebe a mensagem
            #e faz o broadcast para os outros clientes

            #cliente recebe no máximo 2048 bytes
            msg = client.recv(2048)
            broadcast(msg, client)
        except:
            deleteClient(client)
            break

def broadcast(msg, client):
    #Aqui vamos conferir se o nosso cliente atual é diferente do cliente que enviou
    #a mensagem para enviar para ele.
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                deleteClient(client)

def deleteClient(client):
    clients.remove(client)
    #print(f"{client} desconectado")

main()