# Ejercico 4
# Jacob Soto Vilchez

N = input("Pon un entero :")
while (N-(int(N))) > 0:
        print "INCORRECTO, necesitamos un ENTERO(sin punto)"
        N = input("Pon un entero :")
if N%2 == 0:
    print N,"Es Par"
else:
    print N,"Es Impar"
