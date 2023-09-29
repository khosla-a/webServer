# import socket module
from socket import *
# In order to terminate the program
import sys



def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  serverSocket.listen() 

  while True:
   #Establish the connection
   print('Ready to serve...')
   connectionSocket, addr = serverSocket.accept()

   try:
    message = connectionSocket.recv(1024)
    filename = message.split()[1]
    #opens the client requested file. 
    #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
    f = open(filename[1:])
    outputdata = f.read()
    print (outputdata)
   
    connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
    connectionSocket.send(outputdata.encode())

    #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n"

    for i in f: #for line in file
      #Fill in start - append your html file contents #Fill in end 
      serverSocket.send(outputdata[i].encode())
      #Send the content of the requested file to the client (don't forget the headers you created)!
      # Fill in start

      
      # Fill in end

      connectionSocket.close() #closing the connection socket

   except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      outputdata = b"\nHTTP/1.1 404 Not Found\r\n"
      connectionSocket.send(outputdata)
      #Fill in end


      #Close client socket
      #Fill in start
      connectionSocket.close() #closing the connection socket
      #Fill in end


if __name__ == "__main__":
  webServer(13331)

      
      