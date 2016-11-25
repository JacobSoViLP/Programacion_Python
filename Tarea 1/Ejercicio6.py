# Ejercicio 6
# Jacob Soto Vilchez
peso=input("Peso: ")
H=input("Altura(m): ")
imc=peso/(H**2)
if imc<16:
    print "El IMC es de: " + str(imc) + ", Padece Delgadez Severa"
elif imc>=16.00 and imc<16.99:
    print "El IMC es de: " + str(imc) + ", Padece Delgadez Moderada"
elif imc>=17.00 and imc<18.49:
    print "El IMC es de: " + str(imc) + ", Padece Delgadez Leve"
elif imc>=18.5 and imc<24.99:
    print "El IMC es de: " + str(imc) + ", Datos Normales"
elif imc>=25.00 and imc<29.99:
    print "El IMC es de: " + str(imc) + ", Padece Sobrepeso"
elif imc>=30.00 and imc<39.99:
    print "El IMC es de: " + str(imc) + ", Padece de Obesidad"
elif imc>=40.00:
    print "El IMC es de: " + str(imc) + ", Emergencia Medica de Obesidad Morbida"
