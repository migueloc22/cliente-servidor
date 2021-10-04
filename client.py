import os
import socket #traemos la libreria de socket  y declamos el host y el pueto de la conexion
host = "localhost"
puerto = 8081
# distanciamos el objeto socket
socket_cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#conectamos  el socket
socket_cs.connect((host,puerto))
nombre_cliente = input("Escriba su nombre: ")
while True:
    # Recuperamos los valores de teclados
  mensaje_1 = input("Escribé su mensaje "+nombre_cliente+" : ")
  print("...")
  mensaje_1 = nombre_cliente + " mensaje: "+mensaje_1
  # Se va utilizar la funcion de send para enviar para enviar el socket nos obliga en codificarlo en ascii
  socket_cs.send(mensaje_1.encode(encoding="ascii",errors="ignore"))
  # vamos recibir un mensaje de buffer y en la parametrizacion se va recibir 1024 caracteres
  mensaje_receptor = socket_cs.recv(1024)
  # vamos a imprimir y luego a codificar
  print("Respuesta de servidor: ",mensaje_receptor.decode(encoding="ascii",errors="ignore"))
  
socket_cs.close()