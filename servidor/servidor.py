import socket, time
import sys
sys.path.append(r'C:\Users\user\Desktop\InfraCom')
import funcSocket as fs

HOST = '127.0.0.1'
PORT = 50000
BUFFER_SIZE = 1024

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind((HOST, PORT))
print(f'Servidor iniciado em {HOST}:{PORT}')
msg, addr = servidor.recvfrom(BUFFER_SIZE)
time.sleep(0.1)
name = msg.decode()
name = fs.rename_arq(name, 0)
fs.receber_arquivo(('servidor\\' + name), servidor, 0)
time.sleep(0.5)
print('passou pelo rename e está printando ' + name)
fs.enviar_arquivo(name, servidor, addr, 0)

'''op = ['', '']
while op[0] != '3':
    msg, addr = servidor.recvfrom(BUFFER_SIZE)
    time.sleep(0.1)
    name = msg.decode()
    op = name.split('-')  
    if  op[0] == '1':
        name = op[1]
        fs.receber_arquivo(name, servidor, 0)
    elif op[0] == '2':
        name = op[1]
        #name = fs.rename_arq(name, 0) # name = 'servidor\\' + name  -> para não renomear o arquivo no servidor
        fs.enviar_arquivo(name, servidor, addr, 0)
    elif op[0] == '3':
        print('Saindo...')
        break
    else:
        print('Opção inválida. Tente novamente.')'''

servidor.close()