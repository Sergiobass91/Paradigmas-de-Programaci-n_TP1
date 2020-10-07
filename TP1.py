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

    auxDisparoX = 0
    auxDisparoY = 0

    while True:

        datosParticipante['numeroId'] = int(input("Ingrese el número del participante (999 para finalizar): "))
        if datosParticipante['numeroId'] == 999:
            print("Finalizó la carga de participantes")
            break
        else:
            datosParticipante['nombreApellido'] = input("Ingrese el nombre y apellido del participante: ").lower()
            datosParticipante['edad'] = int(input("Ingrese la edad del participante: "))
            datosParticipante['sexo'] = input("Ingrese el sexo del participante: ").upper()
            for disparo in range(3):
                auxDisparoX = float(input(f"Ingrese la coordenada del disparo {disparo+1} en X: "))
                auxDisparoY = float(input(f"Ingrese la coordenada del disparo {disparo+1} en Y: "))
                datosParticipante['ubicacionDisparo'].append(round(distanciaAlOrigen(auxDisparoX, auxDisparoY),2))
                
    print(datosParticipante)
    return datosParticipante

prueba = cargaParticipantes()