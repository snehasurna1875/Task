import socket
PORT = 6060
d=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER =socket.gethostbyname(socket.gethostname())
d.bind((SERVER,PORT))
d.listen(10)

print ("SERVER STARTED LISTENING..........")
connection , address = d.accept()
print (address,"SEVER IS BEEN CONNECTED")
file_name= input(str("PLEASE ENTER THE NAME OF THE FILE TO BE TRANSFERED : "))
file_open = open(file_name , 'rb')
file_data = file_open.read(1024)
connection.send(file_data)
print("Data has been transmitted successfully")
connection.close()
