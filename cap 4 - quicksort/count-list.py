def count_list(array):
    # caso base - array vazio
    if len(array) == 0:
        return 0
    # caso recursivo - soma 1 ao resultado da chamada recursiva com o restante do array
    else:
        return 1 + count_list(array[1:])

# Exemplo de uso:
numeros = [1, 2, 3, 4, 5]
print(f"O número de elementos na lista é: {count_list(numeros)}")
