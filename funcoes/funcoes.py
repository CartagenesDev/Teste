def calculando_IMC(peso,altura):   
    
    imc = peso / (altura*altura)    
    if (imc <= 18.5):
        return imc, "evocê está muito Magro e precisa se alimentar."
    elif (imc > 18.5) and (imc <= 24.9):
        return imc, "você está com o peso ideal, continue se alimentando bem."
    elif (imc > 24.9) and (imc <= 29.9):
        return imc, "você está com um pouco de sobrepeso."
    elif (imc > 29.9) and (imc <= 34.9):
        return imc, "você está com obesidade grau 01, atenção."
    elif (imc > 34.9) and (imc <= 39.9):
        return imc, "você está com obesidade servera grau 02, muita atenção."
    
    else: 
        return imc , "Obesidade morbida grau 03, procure um médico urgente. "
    
    
def obter_valores():
    while True:
        try:# Tenta executar o bloco de código abaixo e captura exceções
            peso = float(input("Digite seu peso em (kg): "))
            if peso <= 0:
                raise ValueError("O peso deve ser maior que zero.")# Levanta uma exceção se o peso for inválido
            altura = float(input("Digite sua altura (m): "))
            if altura <= 0:
                raise ValueError("A altura deve ser maior que zero.")
            return peso, altura
        except ValueError as e:
            print(f"Entrada invalida {e}. Por favor tente novamente.")      
    
print("Vamos calcular seu IMC, digite algumas informações: ")
peso, altura = obter_valores()
imc, mensagem = calculando_IMC(peso, altura)
print(f"Seu IMC é: {imc:.1f} e {mensagem}")






    
   

