# Ejercicio 1
# Jacob Soto Vilchez
import math as m
A1=input ("Dame la Latitud de P1 ")
A2=input ("Dame la Latitud de P2 ")
B1=input ("Dame la Longitud de P1 ")
B2=input ("Dame la Longitud de P2 ")
def rad(x):
    return (x*m.pi)/180
D = 6371.01*m.acos(m.sin(rad(A1))*m.sin(rad(A2))+m.cos(rad(A1))*m.cos(rad(A2))*m.cos(rad(B1)-rad(B2)))
print D, "Kilometros"
