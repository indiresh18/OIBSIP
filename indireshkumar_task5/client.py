import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def receive():
    while True:
        try:    
            message = client.recv(1024).decode()

            if message == "NAME":
                name = input("Enter your name: ")
                client.send(name.encode())

            else:
                print(message)

        except:
            print("Disconnected from server.")
            client.close()
            break


def write():
    while True:
        message = input()

        if message.lower() == "exit":
            client.close()
            break

        client.send(message.encode())


thread1 = threading.Thread(target=receive)
thread1.start()

thread2 = threading.Thread(target=write)
thread2.start()