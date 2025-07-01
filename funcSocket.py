BUFFER_SIZE = 1024
import socket
import os, time

def enviar_arquivo(namefile, socketC, addr, op):
    dirr = ['servidor\\', 'cliente\\']
    print(f'func: Enviando arquivo: {namefile}')
    namefile = dirr[op] + namefile
    with open(namefile, 'rb') as file:
        while True:
            data = file.read(BUFFER_SIZE)
            if not data:
                break
            socketC.sendto(data, addr)
            time.sleep(0.001)
        print(f'Arquivo enviado!')
    socketC.sendto(b'FIM_DO_ARQUIVO', addr)

def receber_arquivo(namefile, socketC, op):
    with open(namefile, 'wb') as file:
        print(f'func: Recebendo arquivo: {namefile[8:]}')
        while True: 
            try:
                data = socketC.recv(BUFFER_SIZE)
                if not data:
                    print('no data')
                    break
                if data == b'FIM_DO_ARQUIVO':
                    print("Arquivo recebido com sucesso!")
                    break
                file.write(data)
            except socket.error as e:
                print(f"Erro ao receber o arquivo: {e}")
                break


def rename_arq(namefile, op):
    #namefile = dirr[op] + namefile
    nome_atual = namefile.split('.')
    novo_nome = nome_atual[0]+str(op)+'.'+nome_atual[1]#dirr[op]+nome_atual[0]+'_n'+'.'+nome_atual[1]
    
    return novo_nome