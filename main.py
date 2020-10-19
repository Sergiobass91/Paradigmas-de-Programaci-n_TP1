#TP1 Paradimas de Programacion
#Sergio Beltran Galvis Comision A

from distancia import distanciaAlOrigen
from  promedio import promedioDisparos
from mejorDisparo import mejorDisparo
import csv


def cargaParticipantes():

    auxDisparoX = 0
    auxDisparoY = 0
    listaParticipantes = []

    while True:

        datosParticipante = {
            'numeroId': 0,
            'nombreApellido': '',
            'edad': 0,
            'sexo': '',
            'ubicacionDisparo': [],
            'mejorDisparo': 0,
            'promedioDisparo': 0
        }
        datosParticipante['numeroId'] = int(input("Ingrese el número del participante (999 para finalizar): "))
        
        #Salida del programa{
        if datosParticipante['numeroId'] == 999:
            if len(listaParticipantes) == 0:
                print("No se cargó ningún participante.")
            print("Finalizó la carga de participantes.")
            break
        #}

        # for i in listaParticipantes:
        #     if datosParticipante['numeroId'] in listaParticipantes[i]['numeroId']:
        #         print("Número de participante ya seleccionado, ingrese otro número de identificación")
        #         datosParticipante['numeroId'] = int(input("Ingrese el número del participante (999 para finalizar): "))

        else:
            datosParticipante['nombreApellido'] = input("Ingrese el nombre y apellido del participante: ").lower()
            datosParticipante['edad'] = int(input("Ingrese la edad del participante: "))
            datosParticipante['sexo'] = input("Ingrese el sexo del participante (F/M): ").upper()
            for disparo in range(3):
                auxDisparoX = float(input(f"Ingrese la coordenada del disparo {disparo+1} en X: "))
                while auxDisparoX < -80 or auxDisparoX > 80:
                    print("Número fuera de rango, ingrese un número entre (-80; 80)")
                    auxDisparoX = float(input(f"Ingrese la coordenada del disparo {disparo+1} en X: "))

                auxDisparoY = float(input(f"Ingrese la coordenada del disparo {disparo+1} en Y: "))
                while auxDisparoY < -80 or auxDisparoY > 80:
                    print("Número fuera de rango, ingrese un número entre (-80; 80)")
                    auxDisparoY = float(input(f"Ingrese la coordenada del disparo {disparo+1} en Y: "))
                
                datosParticipante['ubicacionDisparo'].append(distanciaAlOrigen(auxDisparoX, auxDisparoY))

        datosParticipante['mejorDisparo'] = mejorDisparo(datosParticipante['ubicacionDisparo'])
        datosParticipante['promedioDisparo'] = promedioDisparos(datosParticipante['ubicacionDisparo'])

        listaParticipantes.append(datosParticipante)

    return listaParticipantes

participantes = cargaParticipantes()
print(participantes) #DEBUG

def main():

    print("\n" + "="*40 + "¡¡¡ Podio de Ganadores !!!" + "="*40 + "\n")
    ordenParticipantes = sorted(participantes, key= lambda k:k['mejorDisparo'])
    print(ordenParticipantes) #DEBUG
    print(ordenParticipantes[0]) #DEBUG
    print(ordenParticipantes[0]['numeroId']) #DEBUG
    print(ordenParticipantes[0]['nombreApellido']) #DEBUG
    print(ordenParticipantes[0]['mejorDisparo']) #DEBUG
    podioGanadores = []
    
    with open('podioGanadores.txt', 'w') as txtFile:
        for ganador in ordenParticipantes:
            txtFile.write("PODIO DE GANADORES")

    with open('tablaParticipantes.csv', 'w') as csvfile:
        
        for participante in participantes:
            writer = csv.DictWriter(csvfile, fieldnames= participante.keys())
            writer.writeheader()
            writer.writerows(participantes)
    csvfile.close() 


if __name__ == "__main__":
    main()