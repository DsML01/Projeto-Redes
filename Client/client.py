import threading
import socket

def main():
    #AF_INET = IPV4 e SOCK_STREAM = TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Tenta se conectar com o servidor, na porta 1533
    try:
        client.connect(('localhost', 1533))
    except:
        return print("Não foi possível se conectar ao servidor.")
    
    username = input("Digite aqui o seu username:\n")
    print("Conectado")

    #target = Nome da função
    #args = Argumentos que a função target recebe
    thread1 = threading.Thread(target=receiveMessage, args=[client])
    thread2 = threading.Thread(target=sendMessage, args=[client, username])

    #Executando as threads
    thread1.start()
    thread2.start()

def receiveMessage(client):
    while True:
        try:
            #Transforma o binário em string e printa na tela
            msg = client.recv(2048).decode('utf-8')
            print(msg)
        except:
            print("\nNão foi possível permanecer conectado no servidor!")
            print("Pressione <Enter> para continuar...")
            client.close()
            break

#Vai ficar tentando enviar mensagens para o servidor, capturando o input
def sendMessage(client, username):
    while True:
        try:
            msg = input("\n")
            #Envia a mensagem em binário, transformando string em binário
            #e enviando
            client.send(f'<{username}> {msg}'.encode('utf-8'))
        except:
            return



main()