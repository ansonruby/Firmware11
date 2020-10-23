import socket
def obtener_info_equipo_remoto():

    equipo_remoto = 'sportlife.karrott.cl'
    #print 'El equipo remoto es: ' + equipo_remoto
    try:
        print 'El equipo remoto es: ' + equipo_remoto
        print 'La direccion IP es: ' + str(socket.gethostbyname(equipo_remoto))
    except socket.error, err_msg:
        print 'Error'
        #print err_msg
        #str(equipo_remoto, err_msg)
    

obtener_info_equipo_remoto()
