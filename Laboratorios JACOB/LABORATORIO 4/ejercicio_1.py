#ejercicio 1
# Jacob Soto Vilchez  

import os

def openfile(nombre,n):
	if os.path.isfile(nombre):
		file=open(nombre,"U")
		for i in range(0,n,1):
			c=file.readline()
			if not c: 
				break
			print c
	else:
		print "El archivo no est� en �sta carpeta o el nombre est� mal ecrito"

archivo=raw_input("\n�Cual es el nombre del archivo de .txt?\n")
archivo=archivo+".txt"		
if input("\n�El arcivho est� en la carpeta del arvhivo .py? [si=1,no=0] ")==1:
	pass
else:
	dir=raw_input("Ingrese la direccion del archivo:\n")
	archivo=dir+'\\'+archivo
lineas=int(raw_input("\n�Cuantas lineas del archivo desea ver?\n"))
openfile(archivo,lineas)
raw_input("\nPresione la tecla intro para terminar la ejecucion")