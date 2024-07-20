def achar_elemento(elem, arr):
    achou = False
    
    for i in range(len(arr)):
        if arr[i] == elem:
            achou = True
    if (achou == False):
        print("não encontramos o nome: ", elem)
        
    else:
        print("Achamos o nome: ", elem)  
        
nomes = ["Pedro", "João", "Maria", "Eva"]
achar_elemento("Maria", nomes)                  