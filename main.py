
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',2525))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Conexion desde %s' %str(addr))
    request = conn.recv(1024)
    mensaje= request.decode('utf-8')
    print(mensaje)
    conn.sendall('Vehiculo Velocidad Recibida\n')
    #conn.sendall(response)
    conn.close()
    SPI.run(mensaje) 