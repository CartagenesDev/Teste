
"""titulo = ""
nota = 0
comentarios = ""
opcao = ""


opcao = input("Gostaria de avaliar o filme que acabou de assitir? (sim/não) \n")

if (opcao.lower() in ["sim","s"]):
    titulo = input("escreva o ttulo do filme: ")
    nota = input("Qual nota de 0 a 5 esse filme merece? ")
    resposta = input("Você recomendaria esse filme para uma criançã? (sim/não) ")    
    classificacao = resposta.lower() in ["sim","s"]
    
else:
    print("Obrigado pela preferência")   """
    
    



"""peso = float(input("Digite o seu peso: \n"))
altura = float(input("Digite sua altura: \n"))
mes = input("Digite o mês de referencia:\n")


imc = peso / (altura * altura) 

print(f"Seu imc é: {imc:.1f}")

if (imc < 16.9):
    print("Você está muito abaixo do peso.")
elif (17 <= imc <= 18.4):
    print("Você esta abaixo de peso.")
elif (18.5 <= imc <= 24.9):
    print("Você está no peso normal.")
elif (25 <= imc <= 29.9):
    print("Você está acima do peso")
elif (30 <= imc <= 34.9):
    print("Você tem obesidade grau 1.")
elif (35 <= imc <= 40):
    print("Você tem obesidade grau 2")
else:
    print("Você precisa se tratar urgente.")    """
    
"""def diagonalDifference(arr):
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    for i in range(len(arr)):
        primary_diagonal_sum += arr[i][i]
        secondary_diagonal_sum += arr[i][len(arr) - 1 - i]
    
    return abs(primary_diagonal_sum - secondary_diagonal_sum)

if __name__ == '__main__':
    # Lê o tamanho da matriz
    n = int(input("Digite o tamanho da matriz (n): ").strip())

    arr = []

    # Lê cada linha da matriz
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    # Calcula a diferença das diagonais
    result = diagonalDifference(arr)

    # Imprime o resultado na tela
    print(f"A diferença absoluta das diagonais é: {result}")

    # Alternativamente, para escrever o resultado em um arquivo:
    with open("output.txt", "w") as fptr:
        fptr.write(str(result) + '\n')"""
        
for i in range(20,0,-1):
    if i != 13:
     print("Voce está no ",i,"°")
     




"""contador = 1

while (contador <= 20):
    if contador != 13 :
        print("Voce está no ",contador,"°")
    contador += 1"""
    
"""for i in range(21):
 	i -= 21
  	if i != -13:
        print("andar: ", -i)"""
    
        
