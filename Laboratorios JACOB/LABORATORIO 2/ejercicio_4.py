# Ejercicio 4
# Jacob Soto Vilchez
import math as m
n = input("CUANTOS SON EL NUMERO DE LADOS DEL POLOIGONO ")
while n < 3:
    print "RECUERDA QUE EL NUMERO DE LADOS DE UN POLOIGONO DEVE SER MAYOR A TRES"
    n = input("CUANTOS SON EL NUMERO DE LADOS DEL POLIGONO ")
l = input("DAME LA MEDIDA DEL LADO :")
ejex = input ("CUAL ES EL ORIGEN EN EL EJE X :")
ejey = input ("CUAL ES EL ORIGEN EN EL EJE Y :")
while l < 2:
    print "LE PIDO QUE INGRESE UNA MEDIDA PARA EL LADO MAYOR A 1"
    l = input("INGRESELA AHORA: ")
def cos(angulodec):
    return m.cos(m.radians(angulodec))
def sin(angulodec):
    return m.sin(m.radians(angulodec))
lin = range(0,n)
ANGULAR = ((n-2)*180/n)
M_ANGULAR = ANGULAR/2
ANGULAR_E = 180-ANGULAR
CENTRO = [ejex,ejey]
M_LADOS = l/2
HIPOTENUSA = M_LADOS/cos(M_ANGULAR)
x = []
y = []
PUNTOS = []
for i in(lin):
    VALOR_X = round((CENTRO[0]+((cos(i*ANGULAR_E)*HIPOTENUSA))),2)
    x.append(VALOR_X)
    VALOR_Y = round((CENTRO[1]+((sin(i*ANGULAR_E)*HIPOTENUSA))),2)
    y.append(VALOR_Y)
for i in(lin):
    PUNTO = (x[i],y[i])
    PUNTOS.append(PUNTO)
for i in(lin):
    print "P[" + str(i+1) + "]= ", PUNTOS[i]
