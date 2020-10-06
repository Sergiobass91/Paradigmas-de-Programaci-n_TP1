#TP1 Paradimas de Programacion
#Sergio Beltran Galvis Comision A

import math
from distancia import distanciaAlOrigen

datosParticipante = {
    'numeroId': 0,
    'nombreApellido': '',
    'edad': 0,
    'sexo': '',
    'ubicacionDisparo': []
    }

def cargaParticipantes():

    while True:

        datosParticipante['numeroId'] = int(input("Ingrese el número del participante: "))
        if datosParticipante['numeroId'] == 999:
            break
        else:
            datosParticipante['nombreApellido'] = input("Ingrese el nombre y apellido del participante: ")
            datosParticipante['edad'] = int(input("Ingrese la edad del participante: "))
            datosParticipante['sexo'] = input("Ingrese el sexo del participante: ")
            for disparoX in range(3):
                datosParticipante['ubicacionDisparo'].append(int(input(f"Ingrese la coordenada del disparo en X (disparo{disparoX+1}): ")))
                for disparoY in range(3):
                    datosParticipante['ubicacionDisparo'].append(int(input(f"Ingrese la coordenada del disparo en Y (disparo{disparoY+1}): ")))