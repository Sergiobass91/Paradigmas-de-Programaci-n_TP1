#TP1 Paradimas de Programación
#Sergio Beltrán Galvis Comisión A

from cargaParticipantes import cargaParticipantes
import csv

participantes = cargaParticipantes()

def main():

    cantidadHombres = 0
    cantidadMujeres = 0
    promedioEdadMujeres = 0
    auxPromedioDisparos = 0
    promedioDisparos = 0
    mayorApromedioGral = []

    ordenParticipantes = sorted(participantes, key= lambda k:k['mejorDisparo']) #Ordena por mejor Disparo
    ordenPromedio = sorted(participantes, key= lambda k:k['promedioDisparo'], reverse=True) #Ordena por promedio Disparo (menor a mayor)
    ordenPorEdad = sorted(participantes, key= lambda k:k['edad']) #Ordenada por Edad

    try:
        #Genera CSV informando tabla de datos de todos los participantes incriptos
        with open('tablaParticipantes.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames= participantes[0].keys())
            writer.writeheader()
            writer.writerows(participantes)
        csvfile.close()

        #Genera TXT escribiendo los primeros 3 participantes (valida si hay menos de 3)
        with open('podioGanadores.txt', 'w', encoding="UTF-8") as txtFile:
            txtFile.write( "="*40 + "¡¡¡ PODIO DE GANADDORES !!!" + "="*40 + "\n")
            print("\n" + "="*40 + "¡¡¡ PODIO DE GANADDORES !!!" + "="*40 + "\n")

            if len(ordenParticipantes) >= 3:
                txtFile.writelines(f"1er Lugar\nNúmero Participante: {ordenParticipantes[0]['numeroId']}\nNombre y Apellido: {ordenParticipantes[0]['nombreApellido']}\nMejor Disparo: {ordenParticipantes[0]['mejorDisparo']} \n\n")
                print(f"1er Lugar\nNúmero Participante: {ordenParticipantes[0]['numeroId']}\nNombre y Apellido: {ordenParticipantes[0]['nombreApellido']}\nMejor Disparo: {ordenParticipantes[0]['mejorDisparo']} \n\n")
                txtFile.writelines(f"2do Lugar\nNúmero Participante: {ordenParticipantes[1]['numeroId']}\nNombre y Apellido: {ordenParticipantes[1]['nombreApellido']}\nMejor Disparo: {ordenParticipantes[1]['mejorDisparo']} \n\n")
                print(f"2do Lugar\nNúmero Participante: {ordenParticipantes[1]['numeroId']}\nNombre y Apellido: {ordenParticipantes[1]['nombreApellido']}\nMejor Disparo: {ordenParticipantes[1]['mejorDisparo']} \n\n")
                txtFile.writelines(f"3er Lugar\nNúmero Participante: {ordenParticipantes[2]['numeroId']}\nNombre y Apellido: {ordenParticipantes[2]['nombreApellido']}\nMejor Disparo: {ordenParticipantes[2]['mejorDisparo']} \n")
                print(f"3er Lugar\nNúmero Participante: {ordenParticipantes[2]['numeroId']}\nNombre y Apellido: {ordenParticipantes[2]['nombreApellido']}\nMejor Disparo: {ordenParticipantes[2]['mejorDisparo']} \n")
                txtFile.write("="*107 + "\n")
                print("="*107 + "\n")

                print(f"Último participante:\nNúmero Participante: {ordenPromedio[0]['numeroId']}\nNombre y Apellido: {ordenPromedio[0]['nombreApellido']}\nMejor Disparo: {ordenPromedio[0]['mejorDisparo']}\nPromedio Disparo: {ordenPromedio[0]['promedioDisparo']}\n")

            elif len(ordenParticipantes) < 3 and len(ordenParticipantes) >=2:
                txtFile.writelines(f"1er Lugar\nNúmero Participante: {ordenParticipantes[0]['numeroId']}\nNombre y Apellido: {ordenParticipantes[0]['nombreApellido']}\nMejor Disparo: {ordenParticipantes[0]['mejorDisparo']} \n\n")
                print(f"1er Lugar\nNúmero Participante: {ordenParticipantes[0]['numeroId']}\nNombre y Apellido: {ordenParticipantes[0]['nombreApellido']}\nMejor Disparo: {ordenParticipantes[0]['mejorDisparo']} \n\n")
                txtFile.writelines(f"2do (y último) lugar\nNúmero Participante: {ordenParticipantes[1]['numeroId']}\nNombre y Apellido: {ordenParticipantes[1]['nombreApellido']}\nMejor Disparo: {ordenParticipantes[1]['mejorDisparo']} \n")
                print(f"2do (y último) lugar\nNúmero Participante: {ordenParticipantes[1]['numeroId']}\nNombre y Apellido: {ordenParticipantes[1]['nombreApellido']}\nMejor Disparo: {ordenParticipantes[1]['mejorDisparo']} \n")
                txtFile.write("="*107 + "\n")
                print("="*107 + "\n")

            else:
                txtFile.writelines(f"Único Participante\nNúmero Participante: {ordenParticipantes[0]['numeroId']}\nNombre y Apellido: {ordenParticipantes[0]['nombreApellido']}\nMejor Disparo: {ordenParticipantes[0]['mejorDisparo']} \n")
                print(f"Único Participante\nNúmero Participante: {ordenParticipantes[0]['numeroId']}\nNombre y Apellido: {ordenParticipantes[0]['nombreApellido']}\nMejor Disparo: {ordenParticipantes[0]['mejorDisparo']} \n")
                txtFile.write("="*107 + "\n")
                print("="*107 + "\n")
        txtFile.close()

        for i in participantes:
            if i['sexo'] == 'M':
                cantidadHombres +=1
            if i['sexo'] == 'F':
                promedioEdadMujeres += i['edad']
                cantidadMujeres +=1
            
            auxPromedioDisparos += i['promedioDisparo']
            promedioDisparos = round(auxPromedioDisparos/len(participantes),2)

        for i in ordenPromedio:
            if i['promedioDisparo'] > promedioDisparos:
                mayorApromedioGral.append(i)

        print(f"la cantidad de concursantes fueron: {len(participantes)}\n")
        print(f"La cantidad de hombres concursantes fueron: {cantidadHombres}\n")
        print(f"El promedio de edad de las mujeres concursantes es de: {promedioEdadMujeres/cantidadMujeres}\n")
        print(f"Participantes por edad ascendente: \n{ordenPorEdad}\n")
        print(f"El promedio de todos los disparos es: {promedioDisparos}\n")
        print(f"Participantes con promedio mayor al general: {mayorApromedioGral}\n")

    except:
        print("Sin particintes")

if __name__ == "__main__":
    main()