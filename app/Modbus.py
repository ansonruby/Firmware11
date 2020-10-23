
# -*- coding: utf-8 -*-

#------------------------------------------------------------
# Librerias creadas para multi procesos o hilos -------------
#------------------------------------------------------------

import lib.Control_Archivos2
import lib.Control_Fecha
import lib.Control_Ethernet
import lib.Control_Torniquete
import lib.Seguridad
import lib.Generar_PIN
import time
import commands
import sys

#------------------------------------------------------------
# definiciones para el aplicativo principal -----------------
#------------------------------------------------------------

Inicio_Trama            = "¿"
Fin_Trama               = "?"

#funciones---------------------
F_ID        = "0000"
F_Set_ID    = "0001"
F_Ping      = "0002"
F_Fin_Trama = "0003"


#------------------------------------------------------------

#------------------------------------------------------------
def Pedir_ID(ID):

    print Inicio_Trama + ID + F_ID + "0000" +Fin_Trama


def Ping(ID):

    print Inicio_Trama + ID + F_Ping + "OK" +Fin_Trama
    print "OK" #Inicio_Trama + ID + F_ID + "0000" +Fin_Trama


Pedir_ID("1234")
Ping("1234")
    
