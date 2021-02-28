import socket
PORT = 6060
d=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENT =socket.gethostbyname(socket.gethostname())
d.connect((CLIENT,PORT))
print ("CLIENT IS SUCCESFULLY CONNECTED TO SERVER");

filename= input(str("PLEASE ENTER THE FILE NAME :-"))
file = open (filename, 'wb')
file_data = d.recv(1024)
file.write(file_data)
file.close()
print ("FILE RECIEVED SUCCESFULLY")

