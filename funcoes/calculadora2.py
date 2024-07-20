def calculadora (num1, num2, operacao):
    if operacao == 1:
        return "Soma", num1 + num2
    elif operacao == 2:
        return "Subtração", num1 - num2 
    elif operacao == 3:
        return "Multiplicação", num1 * num2 
    elif operacao == 4:
        if num2 == 0:
            return "Divisão", "não é possivel por zero"
        else:
            return "divisão",  num1 / num2 
       
       
while True:
    print("Digite a operação que você quer executar na calculadora:")
    print("")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    print("")
    operacao = int(input())
    if operacao == 0:
        print("Programa encerrado")
        break
    elif operacao != 1 and operacao != 2 and operacao != 3 and operacao != 4:
        print( "Essa opção não existe.")    
    else:
        print("Digite o primeiro numero: ")
        num1 = float(input())
        print("Digite o segundo numero: ")
        num2 = float(input())
        mensagem, resultado = calculadora(num1, num2, operacao)
        if resultado == "não é possivel por zero":
            print(f"{mensagem}: {resultado}")
            print("")
        else:    
            print(f"O resultado da {mensagem} é {resultado:.1f}")
            print("")