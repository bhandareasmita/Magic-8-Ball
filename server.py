import random
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 1234))

server_socket.listen(5)

responses = [
    'It is certain',
    'It is decidedly'''
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Signs point to yes',
    'Reply hazy try again',
    'Very doubtful',
    'Better not tell you now',
    'Cannot predict now'
]


def magic_8_ball(question):
    random.seed(question)
    return random.choice(responses)


client_socket, addr = server_socket.accept()
print(f"Connection is established with {addr = }")

while True:
    question = client_socket.recv(1024).decode('utf-8')
    if not question:
        break

    response = magic_8_ball(question)

    client_socket.send(response.encode('utf-8'))

client_socket.close()

