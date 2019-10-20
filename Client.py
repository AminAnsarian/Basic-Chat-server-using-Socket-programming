from socket import *
import msvcrt as m

###Amin Ansarian 9223803
######################

def runClient(serverName,serverPort):
    clientSocket = socket(AF_INET , SOCK_STREAM)
    clientSocket.settimeout(0.5)
    print(clientSocket)
    check_flag = True
    quit_flag = True
    status_send_flag = True
    
    try:
        clientSocket.connect((serverName , serverPort))
        print("You are now connected to the server")
        cnflag=1
    except:
        print("Connection Failed, Try Again")
        cnflag=0
    
    if (cnflag==1):
        user_status = input('1- type in your own message, 2- View other user messages\n')
    
    while quit_flag:
        if(user_status == '1'):
            if status_send_flag:
                clientSocket.send(bytes(user_status, 'UTF-8'))
                status_send_flag = False
            while True:
                user_message = input('type in your text...\n')
                if(user_message=="#view"):
                    clientSocket.send(bytes(user_message, 'UTF-8'))
                    print("You are now in view mode:")
                    user_status='2'
                    status_send_flag = True
                    break
                elif(user_message=="#quit"):
                    clientSocket.send(bytes(user_message, 'UTF-8'))
                    clientSocket.close()
                    quit_flag = False
                    break
                else:
                    clientSocket.send(bytes(user_message, 'UTF-8'))
        elif(user_status == '2'):
    
            if (check_flag):
                if status_send_flag:
                    clientSocket.send(bytes(user_status, 'UTF-8'))
                    status_send_flag = False
            try:
                modifiedSentence = clientSocket.recv(4096)
                print(modifiedSentence.decode('UTF-8'))
            except:
                if(m.kbhit()):
                    key = m.getch().decode('UTF-8')
                    if (key == "e"):
                        status_send_flag = True
                        check_flag = True
                        user_status = '1'
                    elif (key == "q"):
                        clientSocket.send(bytes(key, 'UTF-8'))
                        check_flag = True
                        quit_flag = False
                        clientSocket.close()
                        break
                    else:
                        check_flag = False
                        print("wrong key,please enter again")
                else:
                    pass
    
        else:
            user_status = input('invalid status number, Please try again\n'
                                '1- type in your own message, 2- View other user messages\n')

if __name__ == "__main__":
    serverName = 'localhost'
    serverPort = 5000
    runClient(serverName,serverPort)