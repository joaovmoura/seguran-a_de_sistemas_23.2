from socket import *
from Feistel import feistel_cipher

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
#Conecta ao servidor
clientSocket.connect((serverName,serverPort))
#Recebe mensagem do usuario e envia ao servidor
message = input('Digite uma frase: ')
encrypted_message = feistel_cipher(message.encode(), 4)
clientSocket.send(encrypted_message)
#Aguarda mensagem de retorno e a imprime
modifiedMessage, addr = clientSocket.recvfrom(2048)
print("Retorno do Servidor:", modifiedMessage.decode())
clientSocket.close()
