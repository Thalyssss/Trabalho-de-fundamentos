def busca_binaria(lista, valor, inicio, fim):
    if inicio > fim:
        return -1  
    meio = (inicio + fim) // 2 
    
    if lista[meio] == valor:
        return meio
    
    elif valor < lista[meio]:
        return busca_binaria(lista, valor, inicio, meio - 1)
    
    else:
        return busca_binaria(lista, valor, meio + 1, fim)

numeros = [2, 4, 6, 8, 10, 12, 14]
posicao = busca_binaria(numeros, 10, 0, len(numeros) - 1)

if posicao != -1:
    print(f"Valor encontrado na posição {posicao}.")
else:
    print("Valor não encontrado.")