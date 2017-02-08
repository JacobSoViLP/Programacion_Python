# Ejecicio 5
# Jacob Soto Vilchez
segundos=int(input("Dame los segundos que deceas convertir: "))
D=(int(segundos/86400))
H=(int((segundos-(D*86400))/3600))
M=(int((segundos-(D*86400)-(H*3600))/60))
S=(int((segundos-(D*86400)-(H*3600)-(M*60))))
print(str(D)+" Dias "+str(H)+" Horas "+str(M)+" Minutos "+str(S)+" Segundos")
