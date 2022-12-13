nombre = input("como te llamas?")
edad = input("cuantos años tienes?")
while not edad.isdigit():
    edad=input("dijita un numero")
if edad<'25':
 print("Eres estudiante")
elif edad>'25':
  print("eres profesor")
elif edad>='65':
  print("eres master")
  