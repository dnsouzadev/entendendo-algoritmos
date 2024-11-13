
def soma_array(array):
    # caso base - array vazio
    if len(array) == 0:
        return 0
    # caso recursivo - soma primeiro elemento com resto do array
    else:
        return array[0] + soma_array(array[1:])

# Exemplo de uso:
numeros = [1, 2, 3, 4, 5]
print(f"A soma é: {soma_array(numeros)}")
