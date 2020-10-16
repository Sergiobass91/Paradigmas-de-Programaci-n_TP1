import math

def distanciaAlOrigen(disparoX, disparoY):
    
    ubicacionDisparo = round(math.sqrt(pow(disparoX,2) + pow(disparoY, 2)),2)
    
    return ubicacionDisparo