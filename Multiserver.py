import  select,socket,sys,queue

###Amin Ansarian 9223803
########

def all_queue(queue):
    items=""
    while not queue.empty():
        items = items + queue.get() + "\n"
    return items[0:len(items)-1]
def runChat(ip,port):
    server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    server.setblocking(0)
    server.bind((ip , port))
    server.listen(0)
    server.settimeout(0.5)
    inputs = [server]
    outputs = []
    messages = {}
    statuses = {}
    client_number = {}
    identifier = 1
    print("Server is Listening")
    while inputs:
        readable, writable, exeptional = select.select(inputs, outputs, inputs)
        for s in readable:
            if s is server:
                connection, client_address = s.accept()
                connection.setblocking(0)
                inputs.append(connection)
                messages[client_address[1]] = queue.Queue()
                statuses[client_address[1]] = '0'
                client_number[client_address[1]] = identifier
                identifier = identifier + 1
            else:
                data_raw = s.recv(2048)
                data = data_raw.decode('UTF-8')
                if data == '1':
                    print("Use with Code {} is in status write".format(s.getpeername()[1]))
                    statuses[s.getpeername()[1]] = '1'
                elif data == '2':
                    statuses[s.getpeername()[1]] = '2'
                    print("Use with Code {} is in status read".format(s.getpeername()[1]))
                elif data in ['#quit', 'q']:
                    inputs.remove(s)
                elif data == "#view":
                    msg = all_queue(messages[s.getpeername()[1]])
                    s.send(bytes(msg, 'UTF-8'))
                else:
                    for ss in inputs[1:len(inputs)]:
                        if ss != s:
                            data_f = "Client Number {}:".format(client_number[s.getpeername()[1]]) + " " + data
                            messages[ss.getpeername()[1]].put(data_f)
                            if statuses[ss.getpeername()[1]] == '2':
                                msg = all_queue(messages[ss.getpeername()[1]])
                                ss.send(bytes(msg, 'UTF-8'))
                            else:
                                continue


########

if __name__ == "__main__":
    ip = 'localhost'
    port = 5000
    runChat(ip,port)







