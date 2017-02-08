# Proyecto final
# Jacob Soto Vilchez
class Materiales_Cromaticos():
    def __init__(self,rango_inicial,temperatura_inicial):
        self.rango_inicial=rango_inicial
        self.temperatura_inicial=temperatura_inicial
        if self.rango_inicial  > 50 and self.rango_inicial < 65 :
            print "Gracias a ",rango_inicial,"y",temperatura_inicial,"pudiste a entra a Materiales Cromaticos"
            print "Tus tema s a elegir son:"
            print "termocromatica, fotocromatica y hidrocoromatica."
            print "Que tengas suerte encontrando tus dos colores, si es que estan aqui xD"
            print " Hay pistas ocultas en la mayoria de los mensajes solo MIRA LAS FALTAS DE ortografia  "
        else:
            print rango_inicial, "y",temperatura_inicial ,"?  No estas listo ahora"
            print "Piensa en que TEMa se pueden tratar esos numeros e intenta con otros numeros "


    def termocromatica(self,rango_visible,T_temperatura):
      self.temperatura_inicial += T_temperatura
      if self.temperatura_inicial > rango_visible :
          self.temperatura_inicial -= rango_visible
          if self.temperatura_inicial > -10 and self.self.temperatura_inicial < 10 :
              print "FELICIDADES has encontrado el color AZUL"
              print "BUSCA de nuevo AQUI si quieres otra NAriz"
          elif self.temperatura_inicial > 10 and self.temperatura_inicial < 20 :
              print "FELICIDADES has encontrado el color NARANJA "
          elif self.temperatura_inicial > 20 :
              print "no consiguiste ni un color en termocromatica"
              print "piensa MENOS"
      else:
        print "no TE has a alcanzado"


    def Me_rindo(self):
        print " Jajajajajaaj pobre "
        print "Mira las mayusculas en los textos y completa la palabra con lo que se te venga a la mente, por ejemplo:"
        print "si esta escrito: ...tiENESs un error GRANDE... ENE = energia y GRANDE significa que una de los parametros que ocupas escribir son de energia y que ocupan ser valores altos"


    def fotocromatica(self,fuerza_F,temperatura_F):
      self.temperatura_inicial += temperatura_F
      if self.temperatura_inicial >= 1 and self.temperatura_inicial <=5 :
          print "FELICIDADES has encontrado el color NEGRO"
          print "disMINuiste bien la energia del Sol"
          print "Pero se Canso y le dio Hambre"
      else:
          print "FELICIDADES has quedado siego"
          print " trata de hacer MENOS aqui si quieres encontrar algo"


    def hidrocromatica(self,proteccion_H,liquido_H):
      self.rango_inicial += proteccion_H
      if self.rango_inicial < liquido_H:
          Color_H = liquido_H - proteccion_H
          if Color_H >= 10 and Color_H <= 25 :
              print "FELICIDADES has encontrado el color Rosa"
          elif Color_H >25 and Color_H <=30:
              print "FELICIDADES has encontrado el color Rojo"
              print "BUSCA de AQUI si quieres otra ROptura "
      else:
          print "La proteccion que nos ES MUY buena"
          print "Sigues estando seco"
          print " HALLARAS solo DOs ROspuestas aqui"



class Animales_Especiales():
    def __init__(self,defensa_inicial,fecha_inicial):
        self.defensa_inicial=defensa_inicial
        self.fecha_inicial=fecha_inicial
        if fecha_inicial < 0:
            print "vas en sentido CONTRARIO"
        elif fecha_inicial >= 1 and fecha_inicial < 365:
            print "Has entrado a Animales_Especiales, FELICIDADES"
            print "Tus especia a elegir sin Rana_Pac, Zorro_AR,Arania ,Caballo_M"
            print "piensa bien en los numeros que pusiste y que pueden significar Algo para estos animales en comun"
        else:
            print fecha_inicial, "Estas bromiendo conmigo"


    def Rana_Pac(self,defenza_R,edadmax_R):
        self.defensa_inicial += defenza_R
        edad_R = edadmax_R/2
        if self.defensa_inicial < edadmax_R:
            print"la rana esta muerta GRACIAS"
        elif edad_R >8 and edad_R <13 :
            print "FELICIDADES has encontrado el color VERDE"
        else:
            print " No te pueden VER"


    def Zorro_AR(self,fecha_Z,defenza_Z):
        self.fecha_inicial -= fecha_Z
        if defenza_Z > 10:
            print "Prueba denuevo"
        elif self.fecha_inicial >=1 and self.fecha_inicial <=2:
            print "EURECA has encontrado el color MARRON(cafe)"
        else:
            print "Sube UN poco mas"


    def Arania(self,fecha_A,defenza_A):
        self.fecha_inicial += fecha_A
        if self.fecha_inicial > 15 and self.fecha_inicial <25:
            print "FELICIDADES has encontrado el color BALNCO"
        else:
            print defenza_A,"En realidad este dato no lo ocupaBLA en esta especie"
            print "Olvidalo y mejor CORRIGEME"


    def Caballo_M(self,fecha_C,defenza_C):
        self.fecha_inicial -= fecha_C
        self.defensa_inicial -= defenza_C
        if self.defensa_inicial == 0 :
            print "WOOOOOOW FELICIDADES puedes elegir el color que quieras(solo sirve para una vez)"
        elif self.fecha_inicial == 0 :
            print "WOOOOOOW FELICIDADES puedes elegir el color que quieras(solo sirve para una vez)"
        else:
            print "ES mas facil de l0 que crees "
###NO HAY NINGUNA RESTRICCION COMO EN LAS OTRAS DOS CLASES
            print "                                          INSTRUCCIONES           "
            print "   Este juego se trata de encontrar los dos colores que se te han asignado en la parte superior dentro de los temas de:"
            print "                   Reacciones_Quimicas , Materiales_Cromaticos y Animales_Especiales                          "
            print "Empezar a ingresar dos numero al asar dentro de un parentesis para poder abanzar ,pero, solo lo lograras"
            print "si tus numeros son los correctos, los ingresar de estas formas: "
            print "                    Reacciones_Quimicas(n1,n2)"
            print " obtendras o unmensaje con una pista o el nombre del nuevo tema para seguir abanzando, por ejemplo:  "
            print "                     Liberacion(x1,x2)  "
            print " obtendras o un mensaje con PISTAS o un COLOR"
            print "Has iniciado dentro de REACCIONES QUIMICAS"
            print "los temas son:"
            print "Liberacion, Combustion, Disolucion"
            print "Puedes seguir buscando tus colores, en los temas de Animales_Especiales y en Materiales_Cromaticos"
            print "si haci lo deseas"
            print "             Un regalo para ti:"
            print "los colores aqui son 'Todos en uno','El color favorito del Rey del dia' y el ultimo es 'Deja de respira y lo encontraras xD'"
            print "para empezar escribe dos valores para iniciar asi:"
            print "Reacciones_Quimicas(n1,n2)"
class Reacciones_Quimicas():
    def __init__(self,compuesto_inicial,expuestoA_inicial):
        self.compuesto_inicial=compuesto_inicial
        self.expuestoA_inicial=expuestoA_inicial

        print "continua con los temas que se te dieron de Reacciones_Quimicas o intenta entrar en los otros temas(Animales_Especiales o Materiales_Cromaticos)"
    def Liberacion(self,enregia_T,enlace_T):
        self.compuesto_inicial -= enregia_T
        self.compuesto_inicial += enlace_T
        if self.compuesto_inicial > self.expuestoA_inicial:
            print " FELICIDADES has encontrado el color GRIS "
        else:
            print "REStas tu energia y libEras energia de los demas "


    def Combustion(self,liberacion_L,fuente_L):
        self.expuestoA_inicial += fuente_L
        if self.expuestoA_inicial > 1000:
            print "FELICIDADES has encontrado el color AMARILLO"
            print "lanzemos unos unos bellos FUEGOS ARTIFICIAFILES "
        else:
            print " trata de SUBIR a los cielos y MAS alla para poder explotar "


    def Disolucion(self,PH_D,protonacion_D):
        self.expuestoA_inicial += protonacion_D
        if self.expuestoA_inicial > 10:
            "No HAS 10grado crearlos de la mejor forma "
        elif self.expuestoA_inicial == 8 or self.expuestoA_inicial == 9:
            print "FELICIDADES has encontrado el color MORADO"
        else:
            print "solo hay un color con dos bolitas parecido a un infinito"
            print "Seguro que los quieres seguir buscando aqui de NUEVo"
