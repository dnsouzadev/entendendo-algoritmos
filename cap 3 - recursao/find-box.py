# O problema é encontrar a chave dentro das caixas e podendo ter caixas dentro de caixas ou elementos aleatorios.
# pagina 58 do livro entendendo algoritmos entendendo recursao

def procure_pela_chave(caixa):
    for item in caixa:
        if isinstance(item, list):
            procure_pela_chave(item)
        elif item == "chave":
            print("Chave encontrada!")

# Exemplo de uso:
caixas = [
    "papel",
    ["clips", ["chaves", "chave"], "elástico"],
    "caneta",
    ["fita", "tesoura"]
]

procure_pela_chave(caixas)