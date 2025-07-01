import socket, time, os
import sys
sys.path.append(r'C:\Users\user\Desktop\InfraCom')
import funcSocket as fs

HOST = '127.0.0.1'
PORT = 50000
BUFFER_SIZE = 1024

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

'conferir no cliente, enviar receber'

name = input('Digite o nome do arquivo a ser enviado: ')
resp = name
cliente.sendto(resp.encode(), (HOST, PORT))
#name = fs.rename_arq(name, 1) #name = 'cliente\\' + name  -> para não renomear o arquivo no cliente
fs.enviar_arquivo(name, cliente, (HOST, PORT), 1)
time.sleep(0.5)
name2 = fs.rename_arq(name, 1)

print(name2)
name2 = 'cliente\\' + name2
fs.receber_arquivo(name2, cliente, 1)
 
'''
op = 0
while op != 3:
    if op == 1:
        name = input('Digite o nome do arquivo a ser enviado: ')
        resp = str(op) + '-' + name
        cliente.sendto(resp.encode(), (HOST, PORT))
        #name = fs.rename_arq(name, 1) #name = 'cliente\\' + name  -> para não renomear o arquivo no cliente
        fs.enviar_arquivo(name, cliente, (HOST, PORT), 1)
    elif op == 2:
        name = input('Digite o nome do arquivo a ser recebido: ')
        resp = str(op) + '-' + name
        cliente.sendto(resp.encode(), (HOST, PORT))
        fs.receber_arquivo(name, cliente, 1)
    elif op == 3:
        cliente.sendto(b'3', (HOST, PORT))
        print('Saindo...')
        break
    else:
        print('Opção inválida. Tente novamente.')

print('Encerrando conexão...')
'''
cliente.close()