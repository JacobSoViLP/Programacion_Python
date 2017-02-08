#  Ejercicio 2
# Jacob Soto Vilchez
N = input("Dame el numero ")
while N > 9999:
    print"Favor de ingresar un numero menor a 4 digitos"
    N = (input("Dame el numero "))
while N < 1000:
    print"Favor de ingresar un numero de al menos 4 digitos"
    N = (input("Dame el numero "))
N_E = str(N)
Sum = int(N_E[0])+int(N_E[1])+int(N_E[2])+int(N_E[3])
print "La suma de los digitos del numero ingresado es igual a: ",Sum
