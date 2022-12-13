selecionar = input("Que operacion desea realizar - + * /")
numero1= int(input("ingresa un numero"))
numero2 = int(input("ingresa otro numero"))
suma = numero1+numero2
resta= numero1-numero2
multiplicar= numero1*numero2
dividir=numero1/numero2

if (selecionar=="+"):
    print("La suma de los numeros son"+str (suma))
elif(selecionar=="-") :
    print("La resta de los numeros son"+ str (resta)  )
elif(selecionar=="*"):
    print("la multiplicacion de los numeros son" +str(multiplicar) )
elif(selecionar=="/"):
    print("La divicion de los numeros son"+ str (dividir))
