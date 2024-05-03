import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 1234))
print("Connected to Magic-8-ball Server")

while True:
    question = input("Ask your question: \n")
    if question.lower() == 'quit':
        print("Have a nice day!")
        break

    client_socket.send(question.lower().encode('utf-8'))

    answer = client_socket.recv(1024).decode('utf-8')
    print(answer)

client_socket.close()
