def manipular_estoque(arr):
    fechar = False
    while (fechar == False):
        print("\nO que deseja fazer no estoque? Selecione uma opção: ")
        print(" 1 - Para exibir estoque")
        print(" 2 - Alterar produto")
        print(" 3 - adicionar produto")
        print(" 4 - remover produto")
        print(" 5 - Fechar sistema")
        print("")
        opcao = int(input("Digite sua opção: "))
        
        if ( opcao == 1):
            for produto in arr:
                print(produto, end=" ")
        elif ( opcao == 2):
            print("Qual é um indice do produto que você deseja alterar? ") 
            indice = int(input())
            print("Qual o novo produto? ")
            novo_produto = input()
            arr[indice] = novo_produto
            print("Produto ", novo_produto," cadastrado com sucesso." ) 
        elif ( opcao == 3):
            print("Digite o nome do produto: ")
            adc_produto = input()
            arr.append(adc_produto)
            print("Produto adicionado com sucesso.")

        elif (opcao == 4):
            print("Digite o nome do produto que você deseja remover: ")
            rmv_produto = input()
            if rmv_produto in arr:
                arr.remove(rmv_produto)
                print(f"O produto {rmv_produto} foi removido com sucesso")
            else:
                print(f"{rmv_produto}Produto não encontrado")    
            
        elif(opcao == 5):
            fechar = True
            
        else:
            print("Selecione uma opção valida.")    
nomes = ["Pedro", "João", "Maria", "Eva"]            
manipular_estoque(nomes)     
                    



"""nomes = ["Pedro", "João", "Maria", "Eva"]

for nomes in nomes:
    print(nomes, end=", ") """              