intentos=0
numero=0

while numero%2==0 :
    numero=int(input("introduce un numero par"))
if numero%2==1:
 intentos=intentos+1
 if intentos<3:
  print("llevas  "+  str(intentos) + " errores")

 else : 
   print("te equivocaste fin del juego")

    
    




0