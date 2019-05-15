import socket
import os
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

file_name = input("input file name:")

socket.sendto(file_name.encode(), ("192.168.219.136",9003))


f = open(file_name,"rb")
#data = f.read(1024)

current_size = 0 
total_size = os.path.getsize(file_name)

socket.sendto(str(total_size).encode(), ("192.168.219.136",9003))

while(current_size < total_size):
        data = f.read(1024)
        socket.sendto(data, ("192.168.219.136",9003))
        current_size = min(current_size +1024, int(total_size))
        print("current_size / total_size = "+str(current_size) +"/" +str(total_size) + " " + str((current_size/total_size)*100))

        
print("ok\n")
print("file_send_end")

