def pesquisa_binaria(lista, item, inicio=0, fim=None):
    # inicializa o fim na primeira chamada
    if fim is None:
        fim = len(lista) - 1
        
    # caso base - elemento não encontrado
    if inicio > fim:
        return None
        
    # calcula o meio
    meio = (inicio + fim) // 2
    chute = lista[meio]
    
    # caso base - elemento encontrado
    if chute == item:
        return meio
    # caso recursivo - metade inferior    
    elif chute > item:
        return pesquisa_binaria(lista, item, inicio, meio - 1)
    # caso recursivo - metade superior
    else:
        return pesquisa_binaria(lista, item, meio + 1, fim)

# Exemplo de uso:
minha_lista = [1, 3, 5, 7, 9]
print(f"Índice do elemento 3: {pesquisa_binaria(minha_lista, 3)}")
print(f"Índice do elemento 7: {pesquisa_binaria(minha_lista, 7)}")
print(f"Elemento não existente retorna: {pesquisa_binaria(minha_lista, 2)}")
