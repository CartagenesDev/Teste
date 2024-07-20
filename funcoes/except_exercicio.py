nome = input("Digite seu nome completo: ")
while True:
    try:
            
        ano = int(input("Digite o ano de nascimento: "))
        if 1922 <= ano <= 2023:
            idade = 2024 - ano
            print(f"O nome completo do usuario é: {nome}")
            print(f"E sua idade atual é: {idade}")
            break
        else:
            print("Você precisa digitar o ano de nascimento entre 1922 a 2021.")    
    except Exception as erro:
          print("Ocorreu um erro.")
          print(erro)
          print("Tente novamnete.")      
            
    
    
