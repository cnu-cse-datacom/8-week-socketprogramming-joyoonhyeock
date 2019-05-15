import socket

server_socket = socket.socket(socket.AF_INEF, socket.SOCK_DGRAM)
server_socket.bind(("192.168.219.136",9003))

file_name, addr = server_socket.recvfrom(2000)
print("File Name:" + str(file_name.decode()))
file_size, addr = server_socket.recvfrom(2000)
size = file_size.decode()
total_size = int(size)
print("File Size:" + str(total_size))

f = open(file_name,"wb")
current_size = 0
#total_size = int(file_size.decode())

while(current_size < total_size):
    data, addr = server_socket.recvfrom(1024)
    current_size = min(current_size + 1024, int(total_size))
    print("current_size / total_size = " + str(current_size) + "/" + str(total_size) + " " + str((current_size/total_size)*100))
    f.write(data)

