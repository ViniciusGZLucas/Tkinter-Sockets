import tkinter
import json
import random
import threading
import socket

Host = "192.168.86.3"
Port = 1000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((Host,Port))

Rand = random.randint(40,300)
Jogadores = []
coord = (Rand+10, Rand+10, Rand+50, Rand+50)
Nick = input("Digite seu Nick: ")
s.send(json.dumps({"Nick":Nick,"Coord":coord}).encode())

Coords = []
Nicks = []
Coords.append(coord)

def OutrosJogadores():
    global Coords
    while True:
        try:
            a = s.recv(1024).decode()
            print(a)
            a = a.replace("[","").replace("]","")
            a = tuple(map(int,a.split(",")))
            print(a)
            if(a != Coords[0]):
                Coords.append(a)
                for Coord in Coords:
                    DesenharTela(Coord)
        except:
            pass

def DesenharTela(Coord):
    C.create_rectangle(Coord,fill="blue")

def PressedA(event):
    global coord,Coords
    C.delete("all")
    coord = coord[0]-2,coord[1],coord[2]-2,coord[3]
    s.send(json.dumps({"Nick":Nick,"Coord":coord}).encode())
    DesenharTela(coord)

def PressedD(event):
    global coord,Coords
    C.delete("all")
    coord = coord[0]+2,coord[1],coord[2]+2,coord[3]
    s.send(json.dumps({"Nick":Nick,"Coord":coord}).encode())
    DesenharTela(coord)

def PressedW(event):
    global coord,Coords
    C.delete("all")
    coord = coord[0],coord[1]-2,coord[2],coord[3]-2
    s.send(json.dumps({"Nick":Nick,"Coord":coord}).encode())
    DesenharTela(coord)

def PressedS(event):
    global coord,Coords
    C.delete("all")
    coord = coord[0],coord[1]+2,coord[2],coord[3]+2
    s.send(json.dumps({"Nick":Nick,"Coord":coord}).encode())
    DesenharTela(coord)

app = tkinter.Tk()
app.title("Test")
app.geometry("500x600")
C = tkinter.Canvas(app)
C.create_rectangle(coord,fill="blue")
C.pack()

app.bind("<a>",PressedA)
app.bind("<d>",PressedD)
app.bind("<w>",PressedW)
app.bind("<s>",PressedS)

OutrosThread = threading.Thread(target=OutrosJogadores)
OutrosThread.start()

app.mainloop()