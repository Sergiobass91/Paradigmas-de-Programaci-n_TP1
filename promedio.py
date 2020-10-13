def promedioDisparos(disparo):
    suma = 0
    for valor in disparo:
        suma += valor
    
    return suma /len(disparo)
