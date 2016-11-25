# Ejercicio 2
# Jacob Soto Vilchez
INTER=0.04
NuSaldo=0
x=input("Saldo Actual: ")
for i in range(4):
    z=INTER*x
    NuSaldo=x+z
    FiSaldo=NuSaldo+(i*z)
    print FiSaldo
