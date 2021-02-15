import socket
import threading

Host = "192.168.86.3"
Port = 1000

Clientes = []
Coords = []

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((Host,Port))
s.listen()

def Mandar(Clientee,Coord):
    for Cliente in Clientes:
        if(Clientee != Cliente):
            try:
                Cliente.send(Coord)
            except:
                pass
        else:
            pass

def Receber(Cliente):
    while True:
        try:
            Recebido = Cliente.recv(1024)
            if("Atacou - " not in Recebido.decode()):
                Mandar(Cliente,Recebido)
            else:
                pass
        except:
            Ip = str(Cliente).split("raddr=")[1].split(">")[0]
            Clientes.remove(Cliente)
            Cliente.close()
            print(f"O jogador com o Ip{Ip} desconectou.")
            break

def Start():
    while True:
        Conn,Address = s.accept()
        Clientes.append(Conn)
        Conn.send(str(Coords).encode("utf-8"))
        print(f"Um jogador Logou usando o ip{Address}.")
        Mandar(Conn,Conn.recv(1024))
        ReceberThread = threading.Thread(target=Receber,args=(Conn,))
        ReceberThread.start()

print("Ativo")
Start()