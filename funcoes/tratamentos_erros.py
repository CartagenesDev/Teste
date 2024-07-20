print("Digite um numero par:")
while True:
    try:        
        par = int(input())
        if par % 2 == 0:
            print("O numero par digitado foi: ", par)
            break
        else:
            print("O numero digitado não é um numero par")
            print("Insira o numero novamente")    
    except:
        print("Você digitou um caracter, informe um numero par:")
                