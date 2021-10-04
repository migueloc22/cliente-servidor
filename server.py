#servidor
import socket
host = "localhost"
puerto = 8081
# distanciamos el objeto socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,puerto))
server.listen(1)
print("Servidor esperando ...")
active, addr= server.accept()
while True:
  recibido = active.recv(1024)
  print("- ",recibido.decode(encoding="ascii",errors="ignore"))
  enviar = input("Escribe se mensaje servidor: ")
  print('...')
  active.send(enviar.encode(encoding="ascii",errors="ignore"))
active.close() #cerramos el hilo