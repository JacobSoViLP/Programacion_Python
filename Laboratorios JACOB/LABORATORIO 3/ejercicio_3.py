# Ejercicio 3
# Jacob Soto Vilchez
a = input ("dame el entero 1 ")
while (a-(int(a))) > 0:
        print "ingrese denuevo un numero(mayor a 0)"
        a = input ("dame el entero 1 ")
b = input ("dame el entero 2 ")
while (b-int(b)) > 0:
        print "ingrese denuevo un numero(mayor a 0)"
        b = input ("dame el entero 2 ")
b = input ("dame el entero 3 ")
while (c-int(c )) > 0:
        print "ingrese denuevo un numero(mayor a 0)"
        c = input ("dame el entero 3 ")
l=[a,b,c]
d=max(l)
e=min(l)
ubimax=l.index(d)
ubimin=l.index(e)
del l[ubimax]
del l[ubimin]
print "El valor menor :",e
print "El valor medio",l[0]
print "El valor mayor",d
