import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)

clients = []
names = []

print("Server is running...")
print("Waiting for clients...")


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)

            if not message:
                raise Exception()

            timestamp = datetime.now().strftime("[%H:%M]")
            sender = names[clients.index(client)]

            full_message = f"{timestamp} {sender}: {message.decode()}"

            print(full_message)

            broadcast(full_message.encode())

        except:
            index = clients.index(client)
            name = names[index]

            clients.remove(client)
            names.remove(name)

            client.close()

            disconnect = f"{name} left the chat."

            print(disconnect)

            broadcast(disconnect.encode())

            break


while len(clients) < 2:
    client, address = server.accept()

    client.send("NAME".encode())

    name = client.recv(1024).decode()

    names.append(name)
    clients.append(client)

    print(f"{name} connected.")

    thread = threading.Thread(target=handle, args=(client,))
    thread.start()