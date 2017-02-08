# Ejercicio 5
# Jacob Soto Vilchez
Nombre = raw_input('Ingrese nombre' )
A = map(str,n)
Valores = ('a','e','i','o','u','A','E','I','O','U')
if Nombre[0] == Valores[0] or Nombre[0] == Valores[1] or Nombre[0] == Valores[2] or Nombre[0] == Valores[3] or Nombre[0] == Valores[4]:
    print "La palabra esta empesando con una VOCAL"
elif Nombre[0] == Valores[5] or Nombre[0] == Valores[6] or Nombre[0] == Valores[7] or Nombre[0] == Valores[8] or Nombre[0] == Valores[9]:
    print "La palabra esta empesando con una VOCAL"
else:
    print "La palabra NO a comensado con una VOCAL"
