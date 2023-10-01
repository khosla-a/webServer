# import socket module
from socket import *
# In order to terminate the program
import sys



def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen()
  #Fill in end

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
      
      body = f.read()
      
      #Content-Type is an example on how to send a header as bytes. There are more!
      ok = b"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\nConnection: close\r\n\r\n"
      #Status code, Content type, Content length
      
         
      connectionSocket.send(ok)
      connectionSocket.send(body.encode()) 
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      outputdata = b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=UTF-8\nConnection: close\r\n\r\n"
      connectionSocket.send(outputdata)
      #Fill in end
      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

  #Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)