def hola(nombre,numero):
    print("hola programador",nombre,numero)
hola("ferney",1)   

def segundos (hora1,):
    hora= hora1*3600
    minutos=hora1* 60
    print("los segundos son",hora," segundos","Los minutos de la hora son",minutos," minutos") 
segundos(2)

def parametro(palab,n):
    palabra1=palab*n
    print(palabra1)
parametro("ferney ",5)

def minutoss (hora1,):
    minutos= hora1*60
    segundos=hora1* 3600
    print(" los minutos de la hora son",minutos," minutos", ",","Los segundos de la hora son ",segundos," segundos") 
minutoss(1)



def segu(segundos):
    hora=segundos/3600
    minuto=segundos/60
    print ("las horas son",hora," y los minutos son",minuto)
segu(2000368)    

def a (n1,n2):
    cont=0
    for i in range(n1,n2):
        if (i%2==0):
            cont=cont+1   
            print("Los numeros pares son",i)    
    print("Entre los numeros : ",n1,"y",n2,"hay :",cont," pares")         
a(2,20)

def domino (a,z):
    print("DOMINO:")
    for  i in range (a,z):
        for j in range(0,i+1):
            print("/"+str(i)+"/"+str(j))
domino(0,7)

 

