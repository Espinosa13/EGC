# -*- encoding: utf-8 -*-
import Math

def resta(i, j):
    return Math.resta(i,j)

def suma(x, y):
    result = x + y
    return result

if __name__=="__main__":
    if resta(8,6) == 2:
        print("Correctamente ejecutara")
        print("Correcto primera prueba satisfactoria")
    else:
        print("Incorrecto primera prueba")

    if resta(7, 2) == 5:
        print("Correcto segunda prueba")
    else:
        print("Incorrecto segunda prueba")

    if resta(-3, 5) == -8:
        print("Correcto tercera prueba")
    else:
        print("Incorrecto tercera prueba")

    if suma(2, 2) == 4:
        print("Correcto tercera prueba")
    else:
        print("Incorrecto tercera prueba")