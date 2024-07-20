"""for i in range(6):
    if i < 3:
        print()
    else:    
        print("rega a planta ", i)
    
    
cont = 0 

while (cont < 6):   
    if cont < 3:
        print()
    else:    
        print("rega a planta ", cont)
    cont += 1   """
    
    
"""for i in range(6):
    if i != 2 and i != 3:
        print("rega a planta ", i) """
        
"""cont = 0

while (cont < 6):
    if cont !=2 and cont != 3:
        print("rega a planta ", cont)
    cont += 1 """
    
    
"""def mostrarNumero():
  print("Escreva um número menor ou igual a 100")
  num = int(input())
  if (num > 100):
    print("O número precisa ser menor ou igual a 100")
  else:
    print("Boa! você escolheu o número: " + str(num))
mostrarNumero()  """  
    
def mostrarNumero():
  numero_valido = False
 
  while(numero_valido == False):
    try:
      num = int(input())
      if(num > 100):
        print("O número precisa ser menor ou igual a 100")
      elif (num < 0):
          print("O número precisa ser menor ou igual a 100")
            
      else:
        print("Boa! Você escolheu o número: " + str(num))
        numero_valido = True
    except:
      print("Precisa digitar um número inteiro")
print("Escreva um número menor ou igual a 100")      
mostrarNumero()   
print()        