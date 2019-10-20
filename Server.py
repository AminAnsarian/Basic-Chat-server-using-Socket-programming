from socket import *
###########


def runServer(serverport):
    serverSocket = socket(AF_INET , SOCK_STREAM)   #AF_INET: Address family the IP SOCK_STREAM: TCP, datagram(SOCK_DGRAM):UDP
    serverSocket.bind(('',serverport))
    serverSocket.listen(1)
    print("This server is ready to recieve")
    while 1:
        connectionSocket , addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024)
        print(sentence)
        print(addr)
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence )
        connectionSocket.close()
        
if __name__ == "__main__":
    serverport = 12500
    runServer(serverport)